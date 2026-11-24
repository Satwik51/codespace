"""
Practical 05: Singly Linked List
--------------------------------
Implements a Singly Linked List using a user-defined Node class and object
references. Supports insertion (beginning, end, specified position), deletion
(beginning, end, specified position, by value), searching, traversal, and
in-place reversal.
"""


class Node:
    """Node of a Singly Linked List."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly Linked List ADT using Node references."""

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def insert_at_position(self, pos, data):
        """Insert a new node at a 1-based position (1 <= pos <= size + 1)."""
        if pos < 1 or pos > self.size + 1:
            raise IndexError(
                f"Position {pos} out of range. Valid range: 1 to {self.size + 1}."
            )
        if pos == 1:
            self.insert_at_beginning(data)
            return
        if pos == self.size + 1:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        curr = self.head
        step = 1
        while step < pos - 1:
            curr = curr.next
            step += 1
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def delete_from_beginning(self):
        """Delete and return the data of the first node."""
        if self.is_empty():
            raise IndexError("List is empty. Nothing to delete.")
        removed = self.head.data
        self.head = self.head.next
        self.size -= 1
        return removed

    def delete_from_end(self):
        """Delete and return the data of the last node."""
        if self.is_empty():
            raise IndexError("List is empty. Nothing to delete.")
        if self.head.next is None:
            removed = self.head.data
            self.head = None
            self.size -= 1
            return removed

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        removed = curr.next.data
        curr.next = None
        self.size -= 1
        return removed

    def delete_at_position(self, pos):
        """Delete and return the node at a 1-based position (1 <= pos <= size)."""
        if self.is_empty():
            raise IndexError("List is empty. Nothing to delete.")
        if pos < 1 or pos > self.size:
            raise IndexError(
                f"Position {pos} out of range. Valid range: 1 to {self.size}."
            )
        if pos == 1:
            return self.delete_from_beginning()

        curr = self.head
        step = 1
        while step < pos - 1:
            curr = curr.next
            step += 1
        removed = curr.next.data
        curr.next = curr.next.next
        self.size -= 1
        return removed

    def delete_by_value(self, target):
        """Delete the first node with data == target. Returns 1-based pos or -1."""
        if self.is_empty():
            return -1

        if self.head.data == target:
            self.head = self.head.next
            self.size -= 1
            return 1

        curr = self.head
        pos = 2
        while curr.next is not None:
            if curr.next.data == target:
                curr.next = curr.next.next
                self.size -= 1
                return pos
            curr = curr.next
            pos += 1
        return -1

    def search(self, target):
        """Return a list of all 1-based positions where target appears."""
        positions = []
        curr = self.head
        pos = 1
        while curr is not None:
            if curr.data == target:
                positions.append(pos)
            curr = curr.next
            pos += 1
        return positions

    def traverse(self):
        """Return a readable representation of the linked list."""
        if self.is_empty():
            return "Singly Linked List is empty: HEAD -> None"
        parts = []
        curr = self.head
        while curr is not None:
            parts.append(str(curr.data))
            curr = curr.next
        return "HEAD -> " + " -> ".join(parts) + " -> None"

    def reverse(self):
        """Reverse the linked list in-place using three pointers."""
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev


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


def main():
    print("=== Practical 05: Singly Linked List ===")
    sll = SinglyLinkedList()

    try:
        while True:
            print("\n--- Menu ---")
            print(f"Current Size: {sll.size}")
            print("1. Insert at Beginning")
            print("2. Insert at End")
            print("3. Insert at Specified Position (1-based)")
            print("4. Delete from Beginning")
            print("5. Delete from End")
            print("6. Delete at Specified Position (1-based)")
            print("7. Delete by Value (First Occurrence)")
            print("8. Search Element")
            print("9. Traverse (Display List)")
            print("10. Reverse List")
            print("11. Exit")

            choice = read_int("Enter your choice (1-11): ")

            if choice == 1:
                val = read_int("Enter integer value to insert at beginning: ")
                sll.insert_at_beginning(val)
                print(f"Inserted {val} at beginning.")

            elif choice == 2:
                val = read_int("Enter integer value to insert at end: ")
                sll.insert_at_end(val)
                print(f"Inserted {val} at end.")

            elif choice == 3:
                pos = read_int(f"Enter position (1 to {sll.size + 1}): ")
                val = read_int("Enter integer value to insert: ")
                try:
                    sll.insert_at_position(pos, val)
                    print(f"Inserted {val} at position {pos}.")
                except IndexError as err:
                    print(f"Error: {err}")

            elif choice == 4:
                try:
                    removed = sll.delete_from_beginning()
                    print(f"Deleted {removed} from beginning.")
                except IndexError as err:
                    print(f"Error: {err}")

            elif choice == 5:
                try:
                    removed = sll.delete_from_end()
                    print(f"Deleted {removed} from end.")
                except IndexError as err:
                    print(f"Error: {err}")

            elif choice == 6:
                if sll.is_empty():
                    print("Error: List is empty. Nothing to delete.")
                else:
                    pos = read_int(f"Enter position to delete (1 to {sll.size}): ")
                    try:
                        removed = sll.delete_at_position(pos)
                        print(f"Deleted {removed} from position {pos}.")
                    except IndexError as err:
                        print(f"Error: {err}")

            elif choice == 7:
                if sll.is_empty():
                    print("Error: List is empty. Nothing to delete.")
                else:
                    val = read_int("Enter value to delete: ")
                    pos = sll.delete_by_value(val)
                    if pos == -1:
                        print(f"Value {val} not found in the list.")
                    else:
                        print(f"Deleted first occurrence of {val} at position {pos}.")

            elif choice == 8:
                if sll.is_empty():
                    print("List is empty. Nothing to search.")
                else:
                    val = read_int("Enter value to search: ")
                    positions = sll.search(val)
                    if positions:
                        print(f"Found {val} at 1-based position(s): {positions}")
                    else:
                        print(f"Value {val} not found in the list.")

            elif choice == 9:
                print(sll.traverse())

            elif choice == 10:
                if sll.is_empty():
                    print("List is empty. Nothing to reverse.")
                else:
                    sll.reverse()
                    print("List reversed:", sll.traverse())

            elif choice == 11:
                print("Exiting Practical 05. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1 to 11.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
