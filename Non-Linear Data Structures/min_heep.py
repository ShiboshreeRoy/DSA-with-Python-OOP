class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """Insert a value into the heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the smallest value in the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Swap the first (smallest) and last elements
        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_value

    def _heapify_up(self, index):
        """Maintain the heap property from a child to the root."""
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap the current node with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursively heapify up
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """Maintain the heap property from the root to a child."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # Check if the left child is smaller
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Check if the right child is smaller
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # If the smallest is not the current node, swap and continue heapifying
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Example usage
heap = MinHeap()
heap.push(10)
heap.push(5)
smallest = heap.pop()  # Should return 5
print("Smallest:", smallest)  # Output: Smallest: 5
