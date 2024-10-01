# test_math_operations.py
import unittest


def add(a, b):
    return a + b


class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        self.assertEqual(add(-1, -1), -2)

    def test_add_positive_and_negative(self):
        """Test adding a positive and a negative number"""
        self.assertEqual(add(5, -3), 2)

    def test_add_zero(self):
        """Test adding a number with zero"""
        self.assertEqual(add(0, 5), 5)


if __name__ == '__main__':
    unittest.main()
