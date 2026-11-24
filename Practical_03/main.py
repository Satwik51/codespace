class StackADT:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            print("Stack Overflow!")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, "pushed successfully.")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow!")
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print("Popped:", value)

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            print("Top element:", self.stack[self.top])


def parenthesis_matching(expression):
    stack = []

    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def postfix_evaluation(expression):
    stack = []

    for ch in expression.split():
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

    return stack.pop()


# Main Menu
capacity = int(input("Enter Stack Capacity: "))
s = StackADT(capacity)

while True:
    print("\n----- STACK ADT MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check Empty")
    print("5. Check Full")
    print("6. Parenthesis Matching")
    print("7. Postfix Evaluation")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            value = input("Enter value: ")
            s.push(value)

        case 2:
            s.pop()

        case 3:
            s.peek()

        case 4:
            print("Stack is Empty" if s.isEmpty() else "Stack is Not Empty")

        case 5:
            print("Stack is Full" if s.isFull() else "Stack is Not Full")

        case 6:
            exp = input("Enter expression: ")
            if parenthesis_matching(exp):
                print("Balanced Parentheses")
            else:
                print("Not Balanced")

        case 7:
            exp = input("Enter postfix expression (space separated): ")
            print("Result:", postfix_evaluation(exp))

        case 8:
            print("Program Terminated.")
            break

        case _:
            print("Invalid Choice!")