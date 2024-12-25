import unittest
from arrays import arrays

class TestArrays(unittest.TestCase):
    def setUp(self):
        self.arrays = arrays()

    def test_kadane_algorithm(self):
        self.assertEqual(self.arrays.kadane_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.arrays.kadane_algorithm([1, 2, 3, 4]), 10)

if __name__ == "__main__":
    unittest.main()
