import unittest
from app import is_prime

class TestIsPrime(unittest.TestCase):

    def test_positive_case(self):
        # ✅ This will pass
        self.assertTrue(is_prime(7))

    def test_negative_case(self):
        # ❌ This will fail (on purpose)
        self.assertTrue(is_prime(4))  # 4 is not a prime!

if __name__ == '__main__':
    unittest.main()
