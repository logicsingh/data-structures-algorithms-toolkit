import unittest
from dsa_toolkit.linked_list import LinkedList
class LinkedListTests(unittest.TestCase):
    def test_append_prepend_find(self):
        x=LinkedList(); x.append(2); x.prepend(1); x.append(3); self.assertEqual(x.to_list(),[1,2,3]); self.assertEqual(x.find(2),1); self.assertEqual(x.find(8),-1)
    def test_delete_head_middle_tail_missing(self):
        x=LinkedList()
        for v in [1,2,3]: x.append(v)
        self.assertTrue(x.delete(1)); self.assertTrue(x.delete(2)); self.assertTrue(x.delete(3)); self.assertFalse(x.delete(3)); self.assertEqual(x.size(),0); self.assertTrue(x.is_empty())
    def test_delete_empty(self): self.assertFalse(LinkedList().delete(5))
