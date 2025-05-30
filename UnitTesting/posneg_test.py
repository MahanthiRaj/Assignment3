def check_number(x):
    if x > 0:
        return "Positive Number"
    else:
        return "Negative Number"

import unittest

class TestCheckNumber(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(check_number(10), "Positive Number")
        self.assertNotEqual(check_number(1), "Negative Number")
    
    def test_negative(self):
        self.assertEqual(check_number(-5), "Negative Number")
        self.assertNotEqual(check_number(-1), "Positive Number") 

if __name__ == '__main__':
    unittest.main()
