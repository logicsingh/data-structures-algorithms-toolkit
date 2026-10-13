import unittest
from dsa_toolkit.sorting import bubble_sort,selection_sort,insertion_sort,merge_sort
class SortingTests(unittest.TestCase):
    def test_all_sorters(self):
        for fn in [bubble_sort,selection_sort,insertion_sort,merge_sort]:
            with self.subTest(fn=fn.__name__):
                self.assertEqual(fn([5,-1,3,3,0]),[-1,0,3,3,5]); self.assertEqual(fn([]),[]); self.assertEqual(fn([4]),[4])
    def test_input_not_mutated(self):
        values=[3,1,2]
        for fn in [bubble_sort,selection_sort,insertion_sort,merge_sort]: fn(values); self.assertEqual(values,[3,1,2])
