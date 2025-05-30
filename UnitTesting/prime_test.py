

def is_prime_simple(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return True
    
import unittest

class TestIsPrimeSimple(unittest.TestCase):
    def test_not_prime(self):
        self.assertFalse(is_prime_simple(1))
        self.assertFalse(is_prime_simple(0))
        self.assertFalse(is_prime_simple(9))

    def test_prime(self):
        self.assertTrue(is_prime_simple(2))
        self.assertTrue(is_prime_simple(3))

if __name__ == '__main__':
    unittest.main()
