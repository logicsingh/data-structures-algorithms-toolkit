class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Unbalanced numeric BST; duplicate values are ignored."""

    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, value):
        if self._root is None:
            self._root = _Node(value)
            self._size = 1
            return True

        current = self._root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = _Node(value)
                    self._size += 1
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = _Node(value)
                    self._size += 1
                    return True
                current = current.right

    def search(self, value):
        current = self._root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self):
        result = []
        stack = []
        current = self._root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def preorder(self):
        if self._root is None:
            return []
        result = []
        stack = [self._root]
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        return result

    def postorder(self):
        if self._root is None:
            return []
        result = []
        stack = [(self._root, False)]
        while stack:
            current, visited = stack.pop()
            if visited:
                result.append(current.value)
                continue
            stack.append((current, True))
            if current.right is not None:
                stack.append((current.right, False))
            if current.left is not None:
                stack.append((current.left, False))
        return result

    def size(self):
        return self._size

    def is_empty(self):
        return self._root is None
