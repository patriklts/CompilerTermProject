class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):       # Add an item to the top of the stack
        self.stack.append(item)

    def pop(self):              # Remove the top item from the stack and return it
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):             # Return the top item from the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):         # Return True if the stack is empty, False otherwise
        return len(self.stack) == 0

    def size(self):             # Return the number of items in the stack
        return len(self.stack)