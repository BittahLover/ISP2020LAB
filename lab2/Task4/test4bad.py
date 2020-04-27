import unittest
from Task4.task4 import clock
from Task4.task4 import fib

class AddTestCase(unittest.TestCase):
    def test_time(self):
        test = fib(50)
        self.assertEqual(test, 12586269024)


if __name__ == "__name__":
    unittest.main()