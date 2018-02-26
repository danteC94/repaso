import unittest
from roman_to_number import convert_roman_to_decimal


class TestRomanToNumber(unittest.TestCase):
    def test_roman_to_decimal_one(self):
        resultado = convert_roman_to_decimal("I")
        self.assertEqual(resultado, 1)


if __name__ == "__main__":
    unittest.main()
