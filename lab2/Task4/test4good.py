import unittest
from Task4.task4 import fib

class AddTestCase(unittest.TestCase):
    def test_time(self):
        test = fib(100)
        self.assertEqual(test, 354224848179261915075)


if __name__ == "__name__":
    unittest.main()