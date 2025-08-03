import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

if __name__ == "__main__":
    unittest.main()
