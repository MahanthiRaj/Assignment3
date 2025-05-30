def add_numbers(a, b):
    return a + b

import unittest
class TestAddNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_zeros(self):
        self.assertNotEqual(add_numbers(2, 5), 6)


if __name__ == '__main__':
    unittest.main()
