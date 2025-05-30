import unittest

def reverse_string(s):
    if type(s) != str:
        raise ValueError("Input must be a string")
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_reverse_normal(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_palindrome(self):
        self.assertNotEqual(reverse_string("madam"), "mad")

    def test_reverse_invalid_type(self):
        with self.assertRaises(ValueError):
            reverse_string("madam") 
            
if __name__ == '__main__':
    unittest.main()