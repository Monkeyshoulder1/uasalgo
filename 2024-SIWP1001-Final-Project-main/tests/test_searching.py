import unittest
from searching import Searching

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search = Searching()

    def test_linear_search(self):
        self.assertEqual(self.search.linear_search([4, 2, 7, 1, 9], 7), 2)
        self.assertEqual(self.search.linear_search([4, 2, 7, 1, 9], 5), -1)

    def test_binary_search(self):
        sorted_data = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.search.binary_search(sorted_data, 4), 3)
        self.assertEqual(self.search.binary_search(sorted_data, 8), -1)

if __name__ == "__main__":
    unittest.main()
