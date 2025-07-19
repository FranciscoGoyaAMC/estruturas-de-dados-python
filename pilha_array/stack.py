class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def pop(self):
        if self.items:
            top_item = self.items[-1]
            del self.items[-1]
            return top_item
        return None
