class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if not self.is_full():
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
        else:
            print("Error: Circular Queue is full")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return removed_item
        else:
            print("Error: Circular Queue is empty")
            return None

    def front(self):
        if not self.is_empty():
            return self.items[self.front]
        else:
            print("Error: Circular Queue is empty")
            return None

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - (self.front - self.rear - 1)

    def display(self):
        if not self.is_empty():
            if self.front <= self.rear:
                print("Circular Queue:", self.items[self.front:self.rear + 1])
            else:
                print("Circular Queue:", self.items[self.front:] + self.items[:self.rear + 1])
        else:
            print("Circular Queue is empty")


# Example usage of the Circular Queue
circular_queue = CircularQueue(5)

print("Enqueuing elements into the circular queue:")
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.display()

#print("\nFront element of the circular queue:", circular_queue.front())

print("\nDequeuing elements from the circular queue:")
print("Dequeued:", circular_queue.dequeue())
print("Dequeued:", circular_queue.dequeue())
circular_queue.display()

print("\nCircular Queue size:", circular_queue.size())
