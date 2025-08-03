import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calc.add("5"), 5)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_newline_and_comma_delimiters(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_numbers_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2,-3")

if __name__ == "__main__":
    unittest.main()
