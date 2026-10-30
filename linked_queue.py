from node import Node


class LinkedQueue:
    """A queue implemented with linked nodes and front/rear references."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        # A linked queue has no fixed capacity; memory is the practical limit.
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def display(self):
        current = self.front
        elements = []
        while current is not None:
            elements.append(current.value)
            current = current.next
        print("Queue (front to rear):", elements)
