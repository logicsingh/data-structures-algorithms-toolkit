import unittest
from dsa_toolkit.binary_search_tree import BinarySearchTree
class BSTTests(unittest.TestCase):
    def setUp(self):
        self.tree=BinarySearchTree()
        for v in [8,3,10,1,6,14,4,7,13]: self.tree.insert(v)
    def test_insert_search_duplicates(self):
        self.assertTrue(self.tree.search(6)); self.assertFalse(self.tree.search(99)); self.assertFalse(self.tree.insert(6)); self.assertEqual(self.tree.size(),9)
    def test_traversals(self):
        self.assertEqual(self.tree.inorder(),[1,3,4,6,7,8,10,13,14]); self.assertEqual(self.tree.preorder(),[8,3,1,6,4,7,10,14,13]); self.assertEqual(self.tree.postorder(),[1,4,7,6,3,13,14,10,8])
    def test_empty(self):
        t=BinarySearchTree(); self.assertTrue(t.is_empty()); self.assertEqual(t.inorder(),[]); self.assertFalse(t.search(2))


    def test_deep_tree_traversals_do_not_use_python_recursion(self):
        tree = BinarySearchTree()
        for value in range(1200):
            tree.insert(value)

        self.assertEqual(tree.size(), 1200)
        self.assertEqual(len(tree.inorder()), 1200)
        self.assertEqual(tree.preorder()[:3], [0, 1, 2])
        self.assertEqual(tree.postorder()[-3:], [2, 1, 0])
