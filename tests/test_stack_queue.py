import unittest
from dsa_toolkit.stack import Stack
from dsa_toolkit.queue import Queue
class StackQueueTests(unittest.TestCase):
    def test_stack_lifo_and_empty(self):
        s=Stack()
        with self.assertRaises(IndexError): s.pop()
        s.push("A"); s.push("B"); self.assertEqual(s.peek(),"B"); self.assertEqual(s.pop(),"B"); self.assertEqual(s.pop(),"A"); self.assertTrue(s.is_empty())
    def test_queue_fifo_and_empty(self):
        q=Queue()
        with self.assertRaises(IndexError): q.dequeue()
        q.enqueue("A"); q.enqueue("B"); self.assertEqual(q.front(),"A"); self.assertEqual(q.dequeue(),"A"); self.assertEqual(q.dequeue(),"B"); self.assertTrue(q.is_empty())
