import unittest
from Task3.task3 import sub_vectors


class SubTestCase(unittest.TestCase):
    def test_sub(self):
        format_vectors_wrong = sub_vectors([3, 5, 6], [3, 5, 10])
        self.assertEqual(format_vectors_wrong, [0, 0, 4])


if __name__ == "__name__":
    unittest.main()
