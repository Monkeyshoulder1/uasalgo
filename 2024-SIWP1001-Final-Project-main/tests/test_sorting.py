import unittest
from sorting import sorting

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.sorting = sorting()

    def test_insertion_sort(self):
        self.assertEqual(self.sorting.insertion_sort([5, 2, 4, 6, 1]), [1, 2, 4, 5, 6])

    def test_merge_sort(self):
        self.assertEqual(self.sorting.merge_sort([38, 27, 43, 3, 9]), [3, 9, 27, 38, 43])

    def test_quick_sort(self):
        self.assertEqual(self.sorting.quick_sort([10, 7, 8, 9, 1]), [1, 7, 8, 9, 10])

if __name__ == "__main__":
    unittest.main()
