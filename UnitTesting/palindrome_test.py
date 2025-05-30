
def is_palindrome(s):
    return s == s[::-1]

import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("madam"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == '__main__':
    unittest.main()
