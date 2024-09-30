from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, proceso):
        self.queue.append(proceso)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0
