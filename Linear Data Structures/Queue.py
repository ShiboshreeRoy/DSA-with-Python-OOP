class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.queue = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        # Return the front item of the queue without removing it
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of elements in the queue
        return len(self.queue)
    def Dispplay(self):
        return self.queue

# Example usage:
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # Output: 10
print(q.peek())     # Output: 20
print(q.size())     # Output: 2
print(q.Dispplay())