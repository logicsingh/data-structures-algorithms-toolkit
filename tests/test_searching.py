import unittest
from dsa_toolkit.searching import linear_search,binary_search
class SearchTests(unittest.TestCase):
    def test_linear_found_missing_empty_duplicates(self):
        self.assertEqual(linear_search([4,8,2],8),1); self.assertEqual(linear_search([1],2),-1); self.assertEqual(linear_search([],1),-1); self.assertEqual(linear_search([3,3],3),0)
    def test_binary_search(self):
        self.assertEqual(binary_search([1,3,5,7],5),2); self.assertEqual(binary_search([1,3,5],4),-1); self.assertEqual(binary_search([],4),-1); self.assertEqual(binary_search([9],9),0)
