import unittest
from utils.validators import is_valid_number, sanitize_expression


class TestValidators(unittest.TestCase):
    def test_is_valid_number_int(self):
        self.assertTrue(is_valid_number("42"))

    def test_is_valid_number_float(self):
        self.assertTrue(is_valid_number("3.14"))

    def test_is_valid_number_negative(self):
        self.assertTrue(is_valid_number("-7.5"))

    def test_is_valid_number_sci(self):
        self.assertTrue(is_valid_number("1.5e-3"))

    def test_is_valid_number_invalid(self):
        self.assertFalse(is_valid_number("abc"))

    def test_is_valid_number_empty(self):
        self.assertFalse(is_valid_number(""))

    def test_sanitize_expression_basic(self):
        self.assertTrue(sanitize_expression("2+3"))

    def test_sanitize_expression_with_functions(self):
        self.assertTrue(sanitize_expression("sin(30)+cos(60)"))

    def test_sanitize_expression_invalid_chars(self):
        self.assertFalse(sanitize_expression("2+3@5"))

    def test_sanitize_expression_with_letters(self):
        self.assertFalse(sanitize_expression("abc"))
