# Design Min Heap

class MinHeap:
"""
Time Complexity:
      - insert(val): O(log n) due to heapify up
      - getMin(): O(1), accessing root element
      - extractMin(): O(log n) due to heapify down
      - _heapify_up(index): O(log n) moving up the heap
      - _heapify_down(index): O(log n) moving down the heap
      - _swap(i, j), _parent_index(i), _left_child_index(i), _right_child_index(i): O(1)
Space Complexity:
      - O(n) to store n elements in the heap list
"""
    def __init__(self):
        self.heap = []

    def getMin(self):
        return self.heap[0] if self.heap else None

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extractMin(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        min_element = self.heap.pop()
        self._heapify_down(0)
        return min_element

    def _heapify_up(self, index):
        parent = self._parent_index(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = self._parent_index(index)

    def _heapify_down(self, index):
        size = len(self.heap)
        while self._left_child_index(index) < size:
            left = self._left_child_index(index)
            right = self._right_child_index(index)
            min_child = left
            if right < size and self.heap[right] < self.heap[left]:
                min_child = right
            if self.heap[index] > self.heap[min_child]:
                self._swap(index, min_child)
                index = min_child
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent_index(self, i):
        return (i - 1) // 2

    def _left_child_index(self, i):
        return 2 * i + 1

    def _right_child_index(self, i):
        return 2 * i + 2


def test_min_heap():
    h = MinHeap()

    # Test inserting elements
    h.insert(10)
    h.insert(4)
    h.insert(15)
    h.insert(20)
    h.insert(0)
    h.insert(8)

    assert h.getMin() == 0, "getMin should return 0"

    # Test extractMin
    assert h.extractMin() == 0, "extractMin should return 0"
    assert h.getMin() == 4, "New min after removing 0 should be 4"

    assert h.extractMin() == 4, "extractMin should return 4"
    assert h.getMin() == 8, "New min after removing 4 should be 8"

    # Insert more elements
    h.insert(2)
    h.insert(3)
    assert h.getMin() == 2, "After inserting 2 and 3, min should be 2"

    assert h.extractMin() == 2
    assert h.extractMin() == 3
    assert h.extractMin() == 8
    assert h.extractMin() == 10
    assert h.extractMin() == 15
    assert h.extractMin() == 20

    # Heap should now be empty
    assert h.getMin() is None, "Heap should be empty now"
    assert h.extractMin() is None, "extractMin should return None on empty heap"

    print("All test cases passed!")

# Call the test function
test_min_heap()
