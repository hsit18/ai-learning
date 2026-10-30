import unittest
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):

    def test_pi_to_5th_digit(self):
        """Test that the result matches pi to the 5th decimal place."""
        self.assertEqual(calculate_pi(), 3.14159)

    def test_return_type_is_float(self):
        """Test that the return type is a float."""
        self.assertIsInstance(calculate_pi(), float)

    def test_pi_is_greater_than_3(self):
        """Test that the result is greater than 3."""
        self.assertGreater(calculate_pi(), 3)

    def test_pi_is_less_than_4(self):
        """Test that the result is less than 4."""
        self.assertLess(calculate_pi(), 4)


if __name__ == "__main__":
    unittest.main()
