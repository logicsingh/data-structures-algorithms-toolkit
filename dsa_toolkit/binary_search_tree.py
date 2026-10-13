class _Node:
    def __init__(self,value): self.value=value; self.left=None; self.right=None

class BinarySearchTree:
    """Unbalanced numeric BST; duplicate values are ignored."""
    def __init__(self): self._root=None; self._size=0
    def insert(self,value):
        if self._root is None: self._root=_Node(value); self._size=1; return True
        cur=self._root
        while True:
            if value==cur.value: return False
            if value<cur.value:
                if cur.left is None: cur.left=_Node(value); self._size+=1; return True
                cur=cur.left
            else:
                if cur.right is None: cur.right=_Node(value); self._size+=1; return True
                cur=cur.right
    def search(self,value):
        cur=self._root
        while cur is not None:
            if value==cur.value: return True
            cur=cur.left if value<cur.value else cur.right
        return False
    def inorder(self):
        out=[]
        def visit(n):
            if n: visit(n.left); out.append(n.value); visit(n.right)
        visit(self._root); return out
    def preorder(self):
        out=[]
        def visit(n):
            if n: out.append(n.value); visit(n.left); visit(n.right)
        visit(self._root); return out
    def postorder(self):
        out=[]
        def visit(n):
            if n: visit(n.left); visit(n.right); out.append(n.value)
        visit(self._root); return out
    def size(self): return self._size
    def is_empty(self): return self._root is None
