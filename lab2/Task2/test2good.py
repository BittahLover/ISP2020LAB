import unittest
import json
from Task2.task2 import to_json


class AddTestCase(unittest.TestCase):
    def test_tuple(self):
        test = to_json(("Tree", "Apple"))
        self.assertEqual(test, json.dumps(("Tree", "Apple")))


if __name__ == "__name__":
    unittest.main()
