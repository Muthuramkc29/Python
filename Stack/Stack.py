from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# So whats happening here is we are using a Stack data structure to implement reversing the string
# DEQUE from collections used, Deque is which where similar LIST but contains a DOUBLY-LINKED LIST which is awesome
# for escaping the Dynamic array .....




