import unittest
from number_to_roman import number_to_roman

class TestNumberToRoman(unittest.TestCase):
    def test_number_to_roman_one(self):
        result = number_to_roman(1)
        self.assertEqual(result, "I")
    def test_number_to_roman_two(self):
        result = number_to_roman(2)
        self.assertEqual(result, "II")
    def test_number_to_roman_three(self):
        result = number_to_roman(3)
        self.assertEqual(result, "III")
    def test_number_to_roman_four(self):
        result = number_to_roman(4)
        self.assertEqual(result, "IV")
    def test_number_to_roman_five(self):
        result = number_to_roman(5)
        self.assertEqual(result, "V")
    def test_number_to_roman_six(self):
        result = number_to_roman(6)
        self.assertEqual(result, "VI")

if __name__ == "__main__":
    unittest.main()
