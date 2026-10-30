"""ArrayQueue: circular queue on a fixed-size list (FIFO)."""


class ArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0                  # index of the front element
        self.size = 0                   # number of stored elements

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue, the queue is full")
        rear = (self.front + self.size) % len(self.data)   # wrap around
        self.data[rear] = value
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)     # wrap around
        self.size = self.size - 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: nothing to peek")
        return self.data[self.front]

    def __str__(self):
        n = len(self.data)
        logical = [str(self.data[(self.front + i) % n]) for i in range(self.size)]
        physical = ["_" if x is None else str(x) for x in self.data]
        return (f"front -> [{', '.join(logical)}] <- rear\n"
                f"  array: [{', '.join(physical)}]  front index={self.front}, size={self.size}")
