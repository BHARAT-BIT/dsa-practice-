class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            return False

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return value