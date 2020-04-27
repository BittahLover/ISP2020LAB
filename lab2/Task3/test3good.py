import unittest
from Task3.task3 import add_vectors


class AddTestCase(unittest.TestCase):
    def test_sum(self):
        format_vectors = add_vectors([3, 5, 6], [3, 5, 10])
        self.assertEqual(format_vectors, [6, 10, 16])


if __name__ == "__name__":
    unittest.main()
