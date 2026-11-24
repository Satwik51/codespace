class ArrayADT:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def traverse(self):
        print("Array:", self.data[:self.size])

    def insert(self, index, value):
        if self.size == self.capacity:
            print("Array is Full!")
        elif index < 0 or index > self.size:
            print("Invalid Index!")
        else:
            for i in range(self.size - 1, index - 1, -1):
                self.data[i + 1] = self.data[i]

            self.data[index] = value
            self.size += 1
            print("Element Inserted Successfully!")

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Invalid Index!")
        else:
            value = self.data[index]

            for i in range(index, self.size - 1):
                self.data[i] = self.data[i + 1]

            self.size -= 1
            self.data[self.size] = None
            print("Deleted Element:", value)

    def update(self, index, value):
        if index < 0 or index >= self.size:
            print("Invalid Index!")
        else:
            self.data[index] = value
            print("Element Updated!")

    def linear_search(self, key):
        for i in range(self.size):
            if self.data[i] == key:
                return i
        return -1

    def binary_search(self, key):
        low = 0
        high = self.size - 1

        while low <= high:
            mid = (low + high) // 2

            if self.data[mid] == key:
                return mid
            elif key < self.data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


# Main Program
capacity = int(input("Enter Array Capacity: "))
arr = ArrayADT(capacity)

while True:
    print("\n----- ARRAY ADT MENU -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Traverse")
    print("5. Linear Search")
    print("6. Binary Search")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            index = int(input("Enter index: "))
            value = int(input("Enter value: "))
            arr.insert(index, value)

        case 2:
            index = int(input("Enter index to delete: "))
            arr.delete(index)

        case 3:
            index = int(input("Enter index to update: "))
            value = int(input("Enter new value: "))
            arr.update(index, value)

        case 4:
            arr.traverse()

        case 5:
            key = int(input("Enter element to search: "))
            result = arr.linear_search(key)

            if result == -1:
                print("Element Not Found!")
            else:
                print("Element Found at Index:", result)

        case 6:
            key = int(input("Enter element to search: "))

            if arr.size == 0:
                print("Array is Empty!")
            else:
                sorted_array = True

                for i in range(arr.size - 1):
                    if arr.data[i] > arr.data[i + 1]:
                        sorted_array = False
                        break

                if sorted_array:
                    result = arr.binary_search(key)

                    if result == -1:
                        print("Element Not Found!")
                    else:
                        print("Element Found at Index:", result)
                else:
                    print("Array must be sorted for Binary Search!")

        case 7:
            print("Program Terminated!")
            break

        case _:
            print("Invalid Choice!")
