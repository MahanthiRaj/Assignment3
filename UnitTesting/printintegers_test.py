def print_int(x):
    result = ""
    for number in x.split():
        if number.isdigit():
            if result:
                result += "," + number
            else:
                result = number
    return result

x = "There are 24 apples and 12 apples"
print(print_int(x))

import unittest

class TestPrintInt(unittest.TestCase):
    def test_multiple_numbers(self):
        self.assertEqual(print_int("There are 24 apples and 12 apples"), "24,12")
        
        
    def test_not_equal(self):
        self.assertNotEqual(print_int("this is 24"), "24")

if __name__ == "__main__":
    unittest.main()
