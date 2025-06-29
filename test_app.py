import unittest
from app import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(7))
    
    def test_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_less_than_two(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()
