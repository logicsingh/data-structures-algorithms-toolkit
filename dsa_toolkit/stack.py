class Stack:
    """List-backed last-in, first-out (LIFO) stack."""
    def __init__(self): self._items=[]
    def push(self,item): self._items.append(item)
    def pop(self):
        if self.is_empty(): raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()
    def peek(self):
        if self.is_empty(): raise IndexError("Cannot peek at an empty stack.")
        return self._items[-1]
    def is_empty(self): return len(self._items)==0
    def size(self): return len(self._items)
    def to_list(self): return list(self._items)
