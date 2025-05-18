class StackMachine:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data:
            return self.data.pop()
        return -1

    def size(self):
        return len(self.data)

    def empty(self):
        return 1 if not self.data else 0

    def top(self):
        if self.data:
            return self.data[-1]
        return -1
