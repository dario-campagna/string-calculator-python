import unittest
from production import string_calculator


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
