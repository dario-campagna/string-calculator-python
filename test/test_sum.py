import unittest
from production import string_calculator


class TestCommaSeparetedNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(0, string_calculator.add(''))
    
    def test_one_number(self):
        self.assertEqual(1, string_calculator.add('1'))
