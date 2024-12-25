import unittest
from basic import Basic

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.basic = Basic()

    def test_euclid_algorithm(self):
        self.assertEqual(self.basic.euclids_algorithm(48, 18), 6)
        self.assertEqual(self.basic.euclids_algorithm(101, 103), 1)

    def test_huffman_coding(self):
        result = self.basic.huffman_coding("abacabad")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, list) for item in result))

if __name__ == "__main__":
    unittest.main()
