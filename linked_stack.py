from node import Node


class LinkedStack:
    """A stack implemented with linked nodes."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # A linked stack has no fixed capacity; memory is the practical limit.
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def display(self):
        current = self.top
        elements = []
        while current is not None:
            elements.append(current.value)
            current = current.next
        print("Stack (top to bottom):", elements)
