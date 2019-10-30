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

    def test_dash_as_standard_delimiters(self):
        self.assertEqual(35, string_calculator.add('//_\n13_6_9_7'))


class TestExceptionOnNegatives(unittest.TestCase):
    def test_exception_on_one_negative(self):
        with self.assertRaises(RuntimeError) as cm:
            string_calculator.add('-1')

        self.assertEqual('negatives not allowed [-1]', str(cm.exception))

    def test_exception_on_positives_and_one_negative(self):
        with self.assertRaises(RuntimeError) as cm:
            string_calculator.add('4,-2,100')

        self.assertEqual('negatives not allowed [-2]', str(cm.exception))

    def test_exception_on_more_than_one_negative(self):
        with self.assertRaises(RuntimeError) as cm:
            string_calculator.add('9,-52,-42,11')

        self.assertEqual('negatives not allowed [-52, -42]', str(cm.exception))
