class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        if self.size == len(self.items):
            self.items.append(None)
        self.items[self.size] = item
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            item = self.items[self.size - 1]
            self.items[self.size - 1] = None
            self.size -= 1
            return item
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[self.size - 1]
        else:
            return None

    def get_size(self):
        return self.size
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.isEmpty())