import unittest

from Heap import *


class TestHeap(unittest.TestCase):
    def test_init_heap(self):

        heap = Heap()

        self.assertIsNotNone(heap)

    def test_find_parent_when_index_is_even(self):
        h = Heap()
        h.heap = [4, 4, 8, 9, 4, 12, 9, 11, 13]

        parent = h.findParentIndex(2)

        self.assertEqual(1, parent)

    def test_find_parent_when_index_is_odd(self):
        h = Heap()
        h.heap = [4, 4, 8, 9, 4, 12, 9, 11, 13]

        parent = h.findParentIndex(3)

        self.assertEqual(1, parent)

    def test_when_bst_is_preserved(self):

        h = Heap()
        h.heap = [4, 4, 8, 9, 4, 12, 9, 11, 13]

        h.insert(7)
        position = len(h.heap)

        self.assertEqual(10, position)

    def test_insert_when_bst_not_preserved(self):
        h = Heap()
        h.heap = [4, 4, 8, 9, 4, 12, 9, 11, 13, 7, 10]

        h.insert(5)

        self.assertListEqual([4, 4, 5, 9, 4, 8, 9, 11, 13, 7, 10, 12], h.heap)


if __name__ == '__main__':
    unittest.main()
