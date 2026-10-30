"""LinkedQueue: queue on a singly linked list with head and tail references."""

from linked_stack import Node


class LinkedQueue:
    def __init__(self):
        self.front = None               # dequeue from the head
        self.rear = None                # enqueue at the tail

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False                    # no fixed capacity

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node           # first element is both front and rear
        else:
            self.rear.next = node       # link after the old tail
        self.rear = node                # new node becomes the rear

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:          # queue became empty
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.front.value

    def __str__(self):
        if self.is_empty():
            return "[] (empty)"
        items, cur = [], self.front
        while cur is not None:
            items.append(str(cur.value))
            cur = cur.next
        return "front -> " + " -> ".join(items) + " <- rear"
