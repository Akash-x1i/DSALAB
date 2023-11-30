class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")
            return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")
            return None

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)


# Example usage of the queue
queue = Queue()

print("Enqueuing elements into the queue:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()

print("\nFront element of the queue:", queue.front())

print("\nDequeuing elements from the queue:")
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
queue.display()

print("\nQueue size:", queue.size())
