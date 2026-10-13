from collections import deque

class Queue:
    """Deque-backed first-in, first-out (FIFO) queue."""
    def __init__(self): self._items=deque()
    def enqueue(self,item): self._items.append(item)
    def dequeue(self):
        if self.is_empty(): raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()
    def front(self):
        if self.is_empty(): raise IndexError("Cannot read the front of an empty queue.")
        return self._items[0]
    def is_empty(self): return len(self._items)==0
    def size(self): return len(self._items)
    def to_list(self): return list(self._items)
