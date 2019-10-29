import unittest
from production import string_calculator


class TestCommaSeparetedNumbers(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(0, string_calculator.add(''))
    
    def test_one_number(self):
        self.assertEqual(1, string_calculator.add('1'))
        self.assertEqual(2, string_calculator.add('2'))

    def test_two_numbers(self):
        self.assertEqual(3, string_calculator.add('1,2'))
    
    def test_unknown_amount_of_numbers(self):
        self.assertEqual(18, string_calculator.add('10,3,5'))
