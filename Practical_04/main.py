"""
Practical 04: Linear and Circular Queues
----------------------------------------
Implements Linear Queue and Circular Queue using fixed-capacity Python lists
with explicit front and rear pointers, including enqueue, dequeue, peek,
overflow, and underflow handling.
"""


class LinearQueue:
    """Fixed-capacity Linear Queue using explicit front and rear indices."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        """Insert an element at the rear of the Linear Queue."""
        if self.is_full():
            raise OverflowError(
                "Linear Queue Overflow: rear reached end of fixed array."
            )
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.data[self.rear] = item

    def dequeue(self):
        """Remove and return the front element of the Linear Queue."""
        if self.is_empty():
            raise IndexError("Linear Queue Underflow: queue is empty.")
        item = self.data[self.front]
        self.data[self.front] = None

        # Reset pointers only when the queue becomes completely empty
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return item

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Linear Queue Underflow: queue is empty.")
        return self.data[self.front]

    def display(self):
        """Return queue elements along with front/rear pointer states."""
        if self.is_empty():
            return f"Linear Queue is empty (front = {self.front}, rear = {self.rear})."
        elements = []
        i = self.front
        while i <= self.rear:
            elements.append(str(self.data[i]))
            i += 1
        return (
            f"Linear Queue (front -> rear): [{', '.join(elements)}] "
            f"| front = {self.front}, rear = {self.rear}"
        )


class CircularQueue:
    """Fixed-capacity Circular Queue using explicit front and rear indices."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        """Insert an element at the rear using circular wrap-around."""
        if self.is_full():
            raise OverflowError("Circular Queue Overflow: queue is full.")
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = item

    def dequeue(self):
        """Remove and return the front element using circular wrap-around."""
        if self.is_empty():
            raise IndexError("Circular Queue Underflow: queue is empty.")
        item = self.data[self.front]
        self.data[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Circular Queue Underflow: queue is empty.")
        return self.data[self.front]

    def display(self):
        """Return circular queue elements and underlying array slots."""
        if self.is_empty():
            return (
                f"Circular Queue is empty (front = {self.front}, rear = {self.rear})."
            )
        elements = []
        idx = self.front
        while True:
            elements.append(str(self.data[idx]))
            if idx == self.rear:
                break
            idx = (idx + 1) % self.capacity
        return (
            f"Circular Queue (front -> rear): [{', '.join(elements)}] "
            f"| front = {self.front}, rear = {self.rear}, slots = {self.data}"
        )


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


def operate_queue(queue, label):
    """Interactive operation loop for either LinearQueue or CircularQueue."""
    while True:
        print(f"\n--- {label} Operations (Capacity: {queue.capacity}) ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check isEmpty / isFull")
        print("5. Display Queue")
        print("6. Back to Queue Selection")

        choice = read_int("Enter choice (1-6): ")

        if choice == 1:
            val = input("Enter value to enqueue: ").strip()
            if val == "":
                print("Cannot enqueue empty value.")
                continue
            try:
                queue.enqueue(val)
                print(f"Enqueued '{val}'.")
            except OverflowError as err:
                print(f"Error: {err}")

        elif choice == 2:
            try:
                removed = queue.dequeue()
                print(f"Dequeued: '{removed}'")
            except IndexError as err:
                print(f"Error: {err}")

        elif choice == 3:
            try:
                front_val = queue.peek()
                print(f"Front element: '{front_val}'")
            except IndexError as err:
                print(f"Error: {err}")

        elif choice == 4:
            print(f"is_empty(): {queue.is_empty()} | is_full(): {queue.is_full()}")

        elif choice == 5:
            print(queue.display())

        elif choice == 6:
            break

        else:
            print("Invalid choice. Please enter 1 to 6.")


def main():
    print("=== Practical 04: Linear and Circular Queues ===")
    try:
        while True:
            print("\n--- Queue Selection ---")
            print("1. Linear Queue")
            print("2. Circular Queue")
            print("3. Exit")

            choice = read_int("Select queue type (1-3): ")
            if choice == 3:
                print("Exiting Practical 04. Goodbye!")
                break
            if choice not in (1, 2):
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

            while True:
                cap = read_int("Enter fixed capacity (positive integer): ")
                if cap > 0:
                    break
                print("Capacity must be greater than 0.")

            if choice == 1:
                operate_queue(LinearQueue(cap), "Linear Queue")
            else:
                operate_queue(CircularQueue(cap), "Circular Queue")

    except (EOFError, KeyboardInterrupt):
        print("\nProgram interrupted. Exiting cleanly.")


if __name__ == "__main__":
    main()
