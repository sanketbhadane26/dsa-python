class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
s = MinStack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Get Minimum")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            value = int(input("Enter value: "))
            s.push(value)

        case 2:
            s.pop()
            print("Element popped")

        case 3:
            print("Top:", s.top())

        case 4:
            print("Minimum:", s.getMin())

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")