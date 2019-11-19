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


class TestNewLineSeparatedNumbers(unittest.TestCase):
    def test_newline_as_separator(self):
        self.assertEqual(5, string_calculator.add('2\n3'))

    def test_newline_and_comma_separated_numbers(self):
        self.assertEqual(49, string_calculator.add('34,7\n8'))


class TestCustomDelimiter(unittest.TestCase):
    def test_semicolon_as_custom_delimiter(self):
        self.assertEqual(23, string_calculator.add('//;\n11;8;4'))

    def test_dash_as_custom_delimiters(self):
        self.assertEqual(35, string_calculator.add('//_\n13_6_9_7'))

    def test_long_delimiters(self):
        self.assertEqual(6, string_calculator.add('//[***]\n1***2***3'))
        self.assertEqual(6, string_calculator.add('//[++]\n1++2++3'))

    def test_multiple_delimiters(self):
        self.assertEqual(33, string_calculator.add('//[*][%]\n11*20%2'))
        self.assertEqual(42, string_calculator.add('//[---][::]\n31::10---1'))


class TestIgnoreBiggerThan1000(unittest.TestCase):
    def test_ignore_1001(self):
        self.assertEqual(2, string_calculator.add('2,10001'))

    def test_ignore_2000_and_1432(self):
        self.assertEqual(1016, string_calculator.add('2,2000,14,1432,1000'))
