"""
Practical 06: Doubly and Circularly Linked Lists
------------------------------------------------
Implements Doubly Linked List (with forward and backward traversals) and
Circularly Linked List using user-defined node objects and references,
supporting insertion, deletion, search, and traversal operations.
"""


class DLLNode:
    """Node for Doubly Linked List."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly Linked List ADT with head and tail references."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = DLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at_position(self, pos, data):
        """Insert at 1-based position (1 <= pos <= size + 1)."""
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

        new_node = DLLNode(data)
        curr = self.head
        step = 1
        while step < pos - 1:
            curr = curr.next
            step += 1

        next_node = curr.next
        new_node.prev = curr
        new_node.next = next_node
        curr.next = new_node
        next_node.prev = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.is_empty():
            raise IndexError("Doubly Linked List is empty. Nothing to delete.")
        removed = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return removed

    def delete_from_end(self):
        if self.is_empty():
            raise IndexError("Doubly Linked List is empty. Nothing to delete.")
        removed = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return removed

    def delete_at_position(self, pos):
        """Delete at 1-based position (1 <= pos <= size)."""
        if self.is_empty():
            raise IndexError("Doubly Linked List is empty. Nothing to delete.")
        if pos < 1 or pos > self.size:
            raise IndexError(
                f"Position {pos} out of range. Valid range: 1 to {self.size}."
            )
        if pos == 1:
            return self.delete_from_beginning()
        if pos == self.size:
            return self.delete_from_end()

        curr = self.head
        step = 1
        while step < pos:
            curr = curr.next
            step += 1

        removed = curr.data
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
        return removed

    def delete_by_value(self, target):
        """Delete first occurrence of target. Returns 1-based pos or -1."""
        curr = self.head
        pos = 1
        while curr is not None:
            if curr.data == target:
                self.delete_at_position(pos)
                return pos
            curr = curr.next
            pos += 1
        return -1

    def search(self, target):
        """Return list of 1-based positions where target occurs."""
        positions = []
        curr = self.head
        pos = 1
        while curr is not None:
            if curr.data == target:
                positions.append(pos)
            curr = curr.next
            pos += 1
        return positions

    def traverse_forward(self):
        if self.is_empty():
            return "Doubly Linked List is empty."
        parts = []
        curr = self.head
        while curr is not None:
            parts.append(str(curr.data))
            curr = curr.next
        return "Forward : None <- " + " <-> ".join(parts) + " -> None"

    def traverse_backward(self):
        if self.is_empty():
            return "Doubly Linked List is empty."
        parts = []
        curr = self.tail
        while curr is not None:
            parts.append(str(curr.data))
            curr = curr.prev
        return "Backward: None <- " + " <-> ".join(parts) + " -> None"


class CLLNode:
    """Node for Circularly Linked List."""

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Singly Circularly Linked List ADT (tail.next always points to head)."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = CLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    def insert_at_end(self, data):
        new_node = CLLNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def insert_at_position(self, pos, data):
        """Insert at 1-based position (1 <= pos <= size + 1)."""
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

        new_node = CLLNode(data)
        curr = self.head
        step = 1
        while step < pos - 1:
            curr = curr.next
            step += 1
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def delete_from_beginning(self):
        if self.is_empty():
            raise IndexError("Circular Linked List is empty. Nothing to delete.")
        removed = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return removed

    def delete_from_end(self):
        if self.is_empty():
            raise IndexError("Circular Linked List is empty. Nothing to delete.")
        removed = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = self.head
            self.tail = curr
        self.size -= 1
        return removed

    def delete_at_position(self, pos):
        """Delete at 1-based position (1 <= pos <= size)."""
        if self.is_empty():
            raise IndexError("Circular Linked List is empty. Nothing to delete.")
        if pos < 1 or pos > self.size:
            raise IndexError(
                f"Position {pos} out of range. Valid range: 1 to {self.size}."
            )
        if pos == 1:
            return self.delete_from_beginning()
        if pos == self.size:
            return self.delete_from_end()

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
        """Delete first occurrence of target. Returns 1-based pos or -1."""
        if self.is_empty():
            return -1
        curr = self.head
        pos = 1
        while True:
            if curr.data == target:
                self.delete_at_position(pos)
                return pos
            curr = curr.next
            pos += 1
            if curr == self.head:
                break
        return -1

    def search(self, target):
        """Return list of 1-based positions where target occurs."""
        if self.is_empty():
            return []
        positions = []
        curr = self.head
        pos = 1
        while True:
            if curr.data == target:
                positions.append(pos)
            curr = curr.next
            pos += 1
            if curr == self.head:
                break
        return positions

    def traverse(self):
        if self.is_empty():
            return "Circular Linked List is empty."
        parts = []
        curr = self.head
        while True:
            parts.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        return "HEAD -> " + " -> ".join(parts) + f" -> (back to HEAD: {self.head.data})"


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


def doubly_list_menu(dll):
    while True:
        print(f"\n--- Doubly Linked List (Size: {dll.size}) ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position (1-based)")
        print("4. Delete from Beginning")
        print("5. Delete from End")
        print("6. Delete at Position (1-based)")
        print("7. Delete by Value")
        print("8. Search Element")
        print("9. Forward Traversal")
        print("10. Backward Traversal")
        print("11. Back to Main Menu")

        choice = read_int("Enter choice (1-11): ")

        if choice == 1:
            dll.insert_at_beginning(read_int("Enter integer value: "))
            print("Inserted at beginning.")
        elif choice == 2:
            dll.insert_at_end(read_int("Enter integer value: "))
            print("Inserted at end.")
        elif choice == 3:
            pos = read_int(f"Enter position (1 to {dll.size + 1}): ")
            val = read_int("Enter integer value: ")
            try:
                dll.insert_at_position(pos, val)
                print(f"Inserted {val} at position {pos}.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 4:
            try:
                print(f"Deleted {dll.delete_from_beginning()} from beginning.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 5:
            try:
                print(f"Deleted {dll.delete_from_end()} from end.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 6:
            if dll.is_empty():
                print("Error: Doubly Linked List is empty.")
            else:
                pos = read_int(f"Enter position (1 to {dll.size}): ")
                try:
                    print(f"Deleted {dll.delete_at_position(pos)} from position {pos}.")
                except IndexError as err:
                    print(f"Error: {err}")
        elif choice == 7:
            if dll.is_empty():
                print("Error: Doubly Linked List is empty.")
            else:
                val = read_int("Enter value to delete: ")
                pos = dll.delete_by_value(val)
                if pos == -1:
                    print(f"Value {val} not found.")
                else:
                    print(f"Deleted {val} from position {pos}.")
        elif choice == 8:
            if dll.is_empty():
                print("List is empty.")
            else:
                val = read_int("Enter value to search: ")
                pos_list = dll.search(val)
                print(f"Found at position(s): {pos_list}" if pos_list else f"{val} not found.")
        elif choice == 9:
            print(dll.traverse_forward())
        elif choice == 10:
            print(dll.traverse_backward())
        elif choice == 11:
            break
        else:
            print("Invalid choice. Please enter 1 to 11.")


def circular_list_menu(cll):
    while True:
        print(f"\n--- Circularly Linked List (Size: {cll.size}) ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position (1-based)")
        print("4. Delete from Beginning")
        print("5. Delete from End")
        print("6. Delete at Position (1-based)")
        print("7. Delete by Value")
        print("8. Search Element")
        print("9. Traverse Circular List")
        print("10. Back to Main Menu")

        choice = read_int("Enter choice (1-10): ")

        if choice == 1:
            cll.insert_at_beginning(read_int("Enter integer value: "))
            print("Inserted at beginning.")
        elif choice == 2:
            cll.insert_at_end(read_int("Enter integer value: "))
            print("Inserted at end.")
        elif choice == 3:
            pos = read_int(f"Enter position (1 to {cll.size + 1}): ")
            val = read_int("Enter integer value: ")
            try:
                cll.insert_at_position(pos, val)
                print(f"Inserted {val} at position {pos}.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 4:
            try:
                print(f"Deleted {cll.delete_from_beginning()} from beginning.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 5:
            try:
                print(f"Deleted {cll.delete_from_end()} from end.")
            except IndexError as err:
                print(f"Error: {err}")
        elif choice == 6:
            if cll.is_empty():
                print("Error: Circular Linked List is empty.")
            else:
                pos = read_int(f"Enter position (1 to {cll.size}): ")
                try:
                    print(f"Deleted {cll.delete_at_position(pos)} from position {pos}.")
                except IndexError as err:
                    print(f"Error: {err}")
        elif choice == 7:
            if cll.is_empty():
                print("Error: Circular Linked List is empty.")
            else:
                val = read_int("Enter value to delete: ")
                pos = cll.delete_by_value(val)
                if pos == -1:
                    print(f"Value {val} not found.")
                else:
                    print(f"Deleted {val} from position {pos}.")
        elif choice == 8:
            if cll.is_empty():
                print("List is empty.")
            else:
                val = read_int("Enter value to search: ")
                pos_list = cll.search(val)
                print(f"Found at position(s): {pos_list}" if pos_list else f"{val} not found.")
        elif choice == 9:
            print(cll.traverse())
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please enter 1 to 10.")


def main():
    print("=== Practical 06: Doubly and Circularly Linked Lists ===")
    dll = DoublyLinkedList()
    cll = CircularLinkedList()

    try:
        while True:
            print("\n--- Main Menu ---")
            print("1. Operate on Doubly Linked List")
            print("2. Operate on Circularly Linked List")
            print("3. Exit")

            choice = read_int("Enter your choice (1-3): ")
            if choice == 1:
                doubly_list_menu(dll)
            elif choice == 2:
                circular_list_menu(cll)
            elif choice == 3:
                print("Exiting Practical 06. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
