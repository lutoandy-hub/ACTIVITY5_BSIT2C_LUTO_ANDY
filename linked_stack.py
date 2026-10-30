"""LinkedStack: stack built on a singly linked list (push/pop at the head)."""


class Node:
    """Shared by LinkedStack and LinkedQueue."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None                 # head of the list = top of the stack

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False                    # no fixed capacity

    def push(self, value):
        node = Node(value)
        node.next = self.top            # new node points to old top
        self.top = node                 # new node becomes the top

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next        # move top down the chain
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: nothing to peek")
        return self.top.value

    def __str__(self):
        if self.is_empty():
            return "[] (empty)"
        items, cur = [], self.top
        while cur is not None:
            items.append(str(cur.value))
            cur = cur.next
        return "top -> " + " -> ".join(items)
