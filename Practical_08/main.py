"""
Practical 08: Hash Table
------------------------
Implements a fixed-size Hash Table using a suitable hash function.
Demonstrates Separate Chaining (using linked-list buckets) and Open Addressing
via Linear Probing (with tombstone deletion markers) for insertion, searching,
and deletion.
"""


def compute_hash(key, capacity):
    """
    Compute bucket index in [0, capacity - 1].
    Supports integer keys (including negative/zero/large) and string keys.
    """
    if isinstance(key, int):
        return key % capacity
    total = 0
    for ch in str(key):
        total = (total * 31 + ord(ch)) % capacity
    return total


class ChainNode:
    """Linked-list node used in Separate Chaining buckets."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class SeparateChainingHashTable:
    """Fixed-size Hash Table using Separate Chaining."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Hash Table capacity must be a positive integer.")
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return compute_hash(key, self.capacity)

    def insert(self, key, value):
        """
        Insert or update (key, value).
        Returns (bucket_index, status_message).
        """
        idx = self._hash(key)
        curr = self.buckets[idx]
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return idx, f"Updated existing key '{key}' in bucket {idx}."
            curr = curr.next

        collision = self.buckets[idx] is not None
        new_node = ChainNode(key, value)
        new_node.next = self.buckets[idx]
        self.buckets[idx] = new_node
        self.size += 1

        if collision:
            return idx, f"Collision at bucket {idx}! Chained key '{key}'."
        return idx, f"Inserted key '{key}' at bucket {idx}."

    def search(self, key):
        """Search for key. Returns (found: bool, value, bucket_index)."""
        idx = self._hash(key)
        curr = self.buckets[idx]
        while curr is not None:
            if curr.key == key:
                return True, curr.value, idx
            curr = curr.next
        return False, None, idx

    def delete(self, key):
        """Delete key if present. Returns (deleted: bool, value, bucket_index)."""
        idx = self._hash(key)
        curr = self.buckets[idx]
        prev = None
        while curr is not None:
            if curr.key == key:
                if prev is None:
                    self.buckets[idx] = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return True, curr.value, idx
            prev = curr
            curr = curr.next
        return False, None, idx

    def display(self):
        print(f"\nSeparate Chaining Hash Table (size={self.size}, capacity={self.capacity}):")
        i = 0
        while i < self.capacity:
            curr = self.buckets[i]
            if curr is None:
                print(f"  Bucket [{i}]: EMPTY")
            else:
                items = []
                while curr is not None:
                    items.append(f"({curr.key!r}: {curr.value!r})")
                    curr = curr.next
                print(f"  Bucket [{i}]: " + " -> ".join(items))
            i += 1


class LinearProbingHashTable:
    """Fixed-size Hash Table using Open Addressing (Linear Probing)."""

    _DELETED = object()

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Hash Table capacity must be a positive integer.")
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return compute_hash(key, self.capacity)

    def insert(self, key, value):
        """
        Insert or update (key, value) using linear probing.
        Returns (final_index, probe_sequence, status_message).
        """
        start_idx = self._hash(key)
        first_deleted_idx = -1
        probes = []

        step = 0
        while step < self.capacity:
            idx = (start_idx + step) % self.capacity
            probes.append(idx)
            slot = self.table[idx]

            if slot is None:
                target_idx = first_deleted_idx if first_deleted_idx != -1 else idx
                self.table[target_idx] = (key, value)
                self.size += 1
                msg = (
                    f"Inserted key '{key}' at slot {target_idx} "
                    f"(probes: {probes})."
                )
                return target_idx, probes, msg

            if slot is self._DELETED:
                if first_deleted_idx == -1:
                    first_deleted_idx = idx
            elif slot[0] == key:
                self.table[idx] = (key, value)
                return idx, probes, f"Updated existing key '{key}' at slot {idx} (probes: {probes})."

            step += 1

        if first_deleted_idx != -1:
            self.table[first_deleted_idx] = (key, value)
            self.size += 1
            return (
                first_deleted_idx,
                probes,
                f"Inserted key '{key}' into deleted slot {first_deleted_idx} (probes: {probes}).",
            )

        raise OverflowError("Hash Table Overflow: no empty slots available.")

    def search(self, key):
        """Search key using linear probing. Returns (found, value, idx, probes)."""
        start_idx = self._hash(key)
        probes = []
        step = 0
        while step < self.capacity:
            idx = (start_idx + step) % self.capacity
            probes.append(idx)
            slot = self.table[idx]
            if slot is None:
                return False, None, -1, probes
            if slot is not self._DELETED and slot[0] == key:
                return True, slot[1], idx, probes
            step += 1
        return False, None, -1, probes

    def delete(self, key):
        """Delete key by placing a DELETED sentinel. Returns (deleted, value, idx)."""
        start_idx = self._hash(key)
        step = 0
        while step < self.capacity:
            idx = (start_idx + step) % self.capacity
            slot = self.table[idx]
            if slot is None:
                return False, None, -1
            if slot is not self._DELETED and slot[0] == key:
                removed_val = slot[1]
                self.table[idx] = self._DELETED
                self.size -= 1
                return True, removed_val, idx
            step += 1
        return False, None, -1

    def display(self):
        print(f"\nLinear Probing Hash Table (size={self.size}, capacity={self.capacity}):")
        i = 0
        while i < self.capacity:
            slot = self.table[i]
            if slot is None:
                print(f"  Slot [{i}]: EMPTY")
            elif slot is self._DELETED:
                print(f"  Slot [{i}]: <DELETED>")
            else:
                print(f"  Slot [{i}]: ({slot[0]!r}: {slot[1]!r})")
            i += 1


def read_int(prompt):
    """Safely read an integer from user input."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Input cannot be empty. Please enter an integer.")
            continue
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_key(prompt):
    """Read a non-empty key; convert to int if numeric, otherwise keep as str."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Key cannot be empty.")
            continue
        try:
            return int(raw)
        except ValueError:
            return raw


def read_value(prompt):
    """Read a non-empty value string."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Value cannot be empty.")
            continue
        return raw


def operate_chaining(ht):
    while True:
        print(f"\n--- Separate Chaining Hash Table (Capacity: {ht.capacity}) ---")
        print("1. Insert (Key, Value)")
        print("2. Search by Key")
        print("3. Delete by Key")
        print("4. Display Hash Table")
        print("5. Back to Main Menu")

        choice = read_int("Enter choice (1-5): ")
        if choice == 1:
            k = read_key("Enter key (integer or string): ")
            v = read_value("Enter value: ")
            _, msg = ht.insert(k, v)
            print(msg)
        elif choice == 2:
            k = read_key("Enter key to search: ")
            found, val, idx = ht.search(k)
            if found:
                print(f"Found at bucket {idx}: {k!r} -> {val!r}")
            else:
                print(f"Key {k!r} not found (hashed to bucket {idx}).")
        elif choice == 3:
            k = read_key("Enter key to delete: ")
            deleted, val, idx = ht.delete(k)
            if deleted:
                print(f"Deleted ({k!r}: {val!r}) from bucket {idx}.")
            else:
                print(f"Key {k!r} not found (bucket {idx}).")
        elif choice == 4:
            ht.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


def operate_linear_probing(ht):
    while True:
        print(f"\n--- Linear Probing Hash Table (Capacity: {ht.capacity}) ---")
        print("1. Insert (Key, Value)")
        print("2. Search by Key")
        print("3. Delete by Key")
        print("4. Display Hash Table")
        print("5. Back to Main Menu")

        choice = read_int("Enter choice (1-5): ")
        if choice == 1:
            k = read_key("Enter key (integer or string): ")
            v = read_value("Enter value: ")
            try:
                _, _, msg = ht.insert(k, v)
                print(msg)
            except OverflowError as err:
                print(f"Error: {err}")
        elif choice == 2:
            k = read_key("Enter key to search: ")
            found, val, idx, probes = ht.search(k)
            if found:
                print(f"Found at slot {idx}: {k!r} -> {val!r} (probes: {probes})")
            else:
                print(f"Key {k!r} not found (probes: {probes}).")
        elif choice == 3:
            k = read_key("Enter key to delete: ")
            deleted, val, idx = ht.delete(k)
            if deleted:
                print(f"Deleted ({k!r}: {val!r}) from slot {idx} (marked <DELETED>).")
            else:
                print(f"Key {k!r} not found.")
        elif choice == 4:
            ht.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


def main():
    print("=== Practical 08: Hash Table (Separate Chaining & Linear Probing) ===")
    try:
        while True:
            print("\n--- Main Menu ---")
            print("1. Separate Chaining Hash Table")
            print("2. Open Addressing (Linear Probing) Hash Table")
            print("3. Exit")

            choice = read_int("Select mode (1-3): ")
            if choice == 3:
                print("Exiting Practical 08. Goodbye!")
                break
            if choice not in (1, 2):
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            while True:
                cap = read_int("Enter fixed hash table size (positive integer, e.g. 7): ")
                if cap > 0:
                    break
                print("Size must be greater than 0.")

            if choice == 1:
                operate_chaining(SeparateChainingHashTable(cap))
            else:
                operate_linear_probing(LinearProbingHashTable(cap))

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
