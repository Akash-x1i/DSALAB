class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack:", self.items)


# Example usage of the stack
stack = Stack()

print("Pushing elements onto the stack:")
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()

print("\nPeek the top element:", stack.peek())

print("\nPopping elements from the stack:")
print("Popped:", stack.pop())
print("Popped:", stack.pop())
stack.display()

print("\nStack size:", stack.size())

print("\nPeek the top element after pops:")
print("Peeked:", stack.peek())
