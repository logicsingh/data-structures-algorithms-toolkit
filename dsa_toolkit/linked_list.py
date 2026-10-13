class _Node:
    def __init__(self,value): self.value=value; self.next=None

class LinkedList:
    """Singly linked list supporting append, prepend, find, and delete."""
    def __init__(self): self._head=None; self._size=0
    def append(self,value):
        node=_Node(value)
        if self._head is None: self._head=node
        else:
            cur=self._head
            while cur.next is not None: cur=cur.next
            cur.next=node
        self._size+=1
    def prepend(self,value):
        node=_Node(value); node.next=self._head; self._head=node; self._size+=1
    def find(self,value):
        cur=self._head; index=0
        while cur is not None:
            if cur.value==value: return index
            cur=cur.next; index+=1
        return -1
    def delete(self,value):
        if self._head is None: return False
        if self._head.value==value: self._head=self._head.next; self._size-=1; return True
        prev=self._head; cur=prev.next
        while cur is not None:
            if cur.value==value: prev.next=cur.next; self._size-=1; return True
            prev,cur=cur,cur.next
        return False
    def to_list(self):
        out=[]; cur=self._head
        while cur is not None: out.append(cur.value); cur=cur.next
        return out
    def size(self): return self._size
    def is_empty(self): return self._head is None
