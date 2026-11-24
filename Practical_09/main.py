"""
Practical 09: Heap and Priority Queue
-------------------------------------
Implements a Binary Min-Heap using an array representation (without heapq),
supporting insert, extract-min, delete, and bottom-up heapify operations.
Extends the Min-Heap to realize a Priority Queue (with FIFO tie-breaking for
duplicate priorities) and demonstrates the duality between Min-Heaps and
Max-Heaps via key negation.
"""


class MinHeap:
    """Binary Min-Heap implemented using a Python list (0-indexed array)."""

    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def get_min(self):
        """Return the minimum element (root) without removing it."""
        if self.is_empty():
            raise IndexError("Heap Underflow: heap is empty.")
        return self.heap[0]

    def _parent(self, idx):
        return (idx - 1) // 2

    def _left(self, idx):
        return 2 * idx + 1

    def _right(self, idx):
        return 2 * idx + 2

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def heapify_up(self, idx):
        """Restore min-heap property moving upward from idx."""
        while idx > 0:
            p = self._parent(idx)
            if self.heap[idx] < self.heap[p]:
                self._swap(idx, p)
                idx = p
            else:
                break

    def heapify_down(self, idx):
        """Restore min-heap property moving downward from idx."""
        n = len(self.heap)
        while True:
            smallest = idx
            left = self._left(idx)
            right = self._right(idx)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != idx:
                self._swap(idx, smallest)
                idx = smallest
            else:
                break

    def insert(self, value):
        """Insert a new value into the Min-Heap."""
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the minimum element from the Min-Heap."""
        if self.is_empty():
            raise IndexError("Heap Underflow: cannot extract from an empty heap.")
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_val
            self.heapify_down(0)
        return min_val

    def delete_value(self, target):
        """Delete the first occurrence of target from the heap. Returns True if found."""
        idx = -1
        for i, val in enumerate(self.heap):
            if val == target:
                idx = i
                break
        if idx == -1:
            return False

        last_idx = len(self.heap) - 1
        if idx == last_idx:
            self.heap.pop()
            return True

        self.heap[idx] = self.heap.pop()
        # Element moved here could be smaller than parent or larger than children
        parent = self._parent(idx)
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heapify_up(idx)
        else:
            self.heapify_down(idx)
        return True

    def build_heap(self, elements):
        """Build a valid Min-Heap in O(n) time from an arbitrary list."""
        self.heap = [item for item in elements]
        n = len(self.heap)
        # Start from the last non-leaf node down to root
        idx = (n // 2) - 1
        while idx >= 0:
            self.heapify_down(idx)
            idx -= 1

    def display(self):
        if self.is_empty():
            return "Min-Heap is empty: []"
        return f"Min-Heap Array: {self.heap} (min = {self.heap[0]})"


class PriorityQueue(MinHeap):
    """
    Priority Queue built by extending MinHeap.
    Supports:
      - mode='min': smaller priority number = higher urgency (default)
      - mode='max': larger priority number = higher urgency (via key negation)
    Uses an incrementing sequence counter to preserve FIFO order on ties.
    """

    def __init__(self, mode="min"):
        super().__init__()
        if mode not in ("min", "max"):
            raise ValueError("Mode must be 'min' or 'max'.")
        self.mode = mode
        self._counter = 0

    def _effective_priority(self, priority):
        return priority if self.mode == "min" else -priority

    def _original_priority(self, effective_priority):
        return effective_priority if self.mode == "min" else -effective_priority

    def enqueue(self, item, priority):
        """Insert (item, priority) into the priority queue."""
        eff_p = self._effective_priority(priority)
        entry = (eff_p, self._counter, item)
        self._counter += 1
        self.insert(entry)

    def dequeue(self):
        """Remove and return (item, priority) with highest urgency."""
        if self.is_empty():
            raise IndexError("Priority Queue Underflow: queue is empty.")
        eff_p, _, item = self.extract_min()
        return item, self._original_priority(eff_p)

    def peek(self):
        """Return (item, priority) with highest urgency without removing."""
        if self.is_empty():
            raise IndexError("Priority Queue Underflow: queue is empty.")
        eff_p, _, item = self.get_min()
        return item, self._original_priority(eff_p)

    def display_queue(self):
        if self.is_empty():
            return "Priority Queue is empty."
        items = [
            f"(item={entry[2]!r}, priority={self._original_priority(entry[0])})"
            for entry in self.heap
        ]
        return f"PriorityQueue ({self.mode}-priority heap): [{', '.join(items)}]"


def demonstrate_min_max_relationship(values):
    """
    Demonstrate that a Max-Heap can be realized directly using a Min-Heap
    by negating numeric keys: max(S) == -min(-S).
    """
    print("\n--- Relationship Between Min-Heap and Max-Heap ---")
    if len(values) == 0:
        print("Empty input list: both Min-Heap and Max-Heap are empty.")
        return

    min_heap = MinHeap()
    min_heap.build_heap(values)

    negated_values = [-x for x in values]
    max_via_min_heap = MinHeap()
    max_via_min_heap.build_heap(negated_values)

    print(f"Input Values               : {values}")
    print(f"Min-Heap Array             : {min_heap.heap}")
    print(f"Min-Heap of Negated (-x)   : {max_via_min_heap.heap}")
    print(
        f"Max-Heap View (-min(-x))   : {[-x for x in max_via_min_heap.heap]}"
    )

    asc_order = []
    while not min_heap.is_empty():
        asc_order.append(min_heap.extract_min())

    desc_order = []
    while not max_via_min_heap.is_empty():
        desc_order.append(-max_via_min_heap.extract_min())

    print(f"Repeated Extract-Min       : {asc_order}")
    print(f"Repeated Extract-Max (-x)  : {desc_order}")


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


def read_int_list(prompt):
    """Safely read space-separated integers (empty input returns [])."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return []
        parts = raw.split()
        nums = []
        ok = True
        for tok in parts:
            try:
                nums.append(int(tok))
            except ValueError:
                print(f"Invalid integer token: '{tok}'. Please re-enter.")
                ok = False
                break
        if ok:
            return nums


def min_heap_menu(heap):
    while True:
        print(f"\n--- Binary Min-Heap Menu (Size: {heap.size()}) ---")
        print("1. Insert Element")
        print("2. Extract Minimum")
        print("3. Peek Minimum")
        print("4. Delete Specific Value")
        print("5. Build Heap from List (Heapify)")
        print("6. Display Heap Array")
        print("7. Back to Main Menu")

        choice = read_int("Enter choice (1-7): ")
        if choice == 1:
            val = read_int("Enter integer to insert: ")
            heap.insert(val)
            print(f"Inserted {val}.")
        elif choice == 2:
            try:
                print(f"Extracted min: {heap.extract_min()}")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 3:
            try:
                print(f"Current min: {heap.get_min()}")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 4:
            if heap.is_empty():
                print("Heap is empty. Nothing to delete.")
            else:
                val = read_int("Enter value to delete: ")
                if heap.delete_value(val):
                    print(f"Deleted {val} and restored heap property.")
                else:
                    print(f"Value {val} not found in heap.")
        elif choice == 5:
            vals = read_int_list("Enter space-separated integers to heapify: ")
            heap.build_heap(vals)
            print("Built Min-Heap:", heap.display())
        elif choice == 6:
            print(heap.display())
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please enter 1 to 7.")


def priority_queue_menu():
    print("\nSelect Priority Queue Mode:")
    print("1. Min-Priority (lower number = higher priority)")
    print("2. Max-Priority (higher number = higher priority, via negated Min-Heap)")
    while True:
        m = read_int("Enter mode (1 or 2): ")
        if m in (1, 2):
            break
        print("Please enter 1 or 2.")

    pq = PriorityQueue("min" if m == 1 else "max")

    while True:
        print(f"\n--- Priority Queue Menu ({pq.mode.upper()}-priority, Size: {pq.size()}) ---")
        print("1. Enqueue (Item, Priority)")
        print("2. Dequeue Highest-Priority Item")
        print("3. Peek Highest-Priority Item")
        print("4. Display Priority Queue")
        print("5. Back to Main Menu")

        choice = read_int("Enter choice (1-5): ")
        if choice == 1:
            item = input("Enter item name/label: ").strip()
            if item == "":
                print("Item cannot be empty.")
                continue
            prio = read_int("Enter integer priority: ")
            pq.enqueue(item, prio)
            print(f"Enqueued '{item}' with priority {prio}.")
        elif choice == 2:
            try:
                item, prio = pq.dequeue()
                print(f"Dequeued: '{item}' (priority = {prio})")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 3:
            try:
                item, prio = pq.peek()
                print(f"Top item: '{item}' (priority = {prio})")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 4:
            print(pq.display_queue())
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


def main():
    print("=== Practical 09: Binary Min-Heap and Priority Queue ===")
    heap = MinHeap()

    try:
        while True:
            print("\n--- Main Menu ---")
            print("1. Binary Min-Heap Operations")
            print("2. Priority Queue Operations")
            print("3. Demonstrate Min-Heap vs Max-Heap Relationship")
            print("4. Exit")

            choice = read_int("Enter your choice (1-4): ")
            if choice == 1:
                min_heap_menu(heap)
            elif choice == 2:
                priority_queue_menu()
            elif choice == 3:
                vals = read_int_list(
                    "Enter integers separated by spaces (or Enter for sample [15 3 27 8 12 1]): "
                )
                if not vals:
                    vals = [15, 3, 27, 8, 12, 1]
                demonstrate_min_max_relationship(vals)
            elif choice == 4:
                print("Exiting Practical 09. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 to 4.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
