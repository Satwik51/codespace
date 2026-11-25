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
            return None
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return None
        else:
            return self.stack[self.top]

def parenthesis_matching(expression):
    s = StackADT(capacity)

    for ch in expression:
        if ch == '(' or ch == '{' or ch == '[':
            s.push(ch)

        elif ch == ')' or ch == '}' or ch == ']':
            if s.isEmpty():
                return False

            top = s.pop()

            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False
    return s.isEmpty()


def postfix_evaluation(expression):
    s=StackADT(capacity)

    for ch in expression.split():
        if ch.isdigit():
            s.push(int(ch))
        else:
            b = s.pop()
            a = s.pop()

            if ch == '+':
                s.push(a + b)
            elif ch == '-':
                s.push(a - b)
            elif ch == '*':
                s.push(a * b)
            elif ch == '/':
                s.push(a / b)

    return s.pop()


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
            value = s.pop()
            if value is not None:
                print("Popped:", value)

        case 3:
            value = s.peek()
            if value is not None:
                print("Top element:", value)

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