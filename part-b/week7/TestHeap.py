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

        self.assertEqual(0, parent)

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

    def test_extract_min(self):
        h = Heap()
        h.heap = [4, 4, 8, 9, 4, 12, 9, 11, 13]

        min = h.extract_root()

        self.assertEqual(min, 4)
        self.assertListEqual(h.heap, [4, 4, 8, 9, 13, 12, 9, 11])

    def test_extract_max(self):
        h = Heap(isMaxHeap=True)
        h.heap = [-13, -12, -11, -9, -9, -8, -4, -4, -4]

        max = h.extract_root()

        self.assertEqual(max, 13)
        self.assertListEqual(h.heap, [-12, -9, -11, -4, -9, -8, -4, -4])


if __name__ == '__main__':
    unittest.main()
