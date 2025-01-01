class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        '''Bo'sh ekanligini tekshirish'''
        return len(self.stack) == 0

    def push(self, data):
        '''Element qo'shish'''
        self.stack.append(data)
        return True

    def pop(self):
        '''Elementni olish'''
        if self.isEmpty():
            return "Stack bo'sh"
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack bo'sh"
        else:
            return self.stack[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.pop())
print(stack.isEmpty())