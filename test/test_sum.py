import unittest
from production import string_calculator


class TestSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(0, string_calculator.add(''))