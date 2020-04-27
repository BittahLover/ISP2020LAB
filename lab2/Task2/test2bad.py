import unittest
from Task2.task2 import to_json


class AddTestCase(unittest.TestCase):
    def test_dictionary_wrong(self):
        test = to_json({"Task", 'Taska'})
        self.assertEqual(test, "incorrect input")


if __name__ == "__name__":
    unittest.main()
