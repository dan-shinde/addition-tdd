import unittest
from addition import add

class TestAddFunction(unittest.TestCase):
    """
    Test the add function
    """
    def test_add_empty_string(self):
        """
        Test that the add function returns 0 for an empty string
        """
        self.assertEqual(add(""), 0)

    def test_add_single_number(self):
        """
        Test that the add function returns the number for a single number
        """
        self.assertEqual(add("1"), 1)

    def test_add_two_numbers(self):
        """
        Test that the add function returns the sum of two numbers
        """
        self.assertEqual(add("1,2"), 3)

    def test_add_multiple_numbers(self):
        """
        Test that the add function returns the sum of multiple numbers
        """
        self.assertEqual(add("1,2,3,4"), 10)

    def test_add_newline_separator(self):
        """
        Test that the add function returns the sum of numbers separated by a newline
        """
        self.assertEqual(add("1\n2,3"), 6)

    def test_add_custom_separator(self):
        """
        Test that the add function returns the sum of numbers separated by a custom separator
        The custom separator is defined by a string starting with "//" and ending with "\n"
        """
        self.assertEqual(add("//;\n1;2"), 3)

    def test_add_custom_separator_multiple_numbers(self):
        """
        Test that the add function returns the sum of numbers separated by a custom separator
        The custom separator is defined by a string starting with "//" and ending with "\n"
        """
        self.assertEqual(add("//;\n1;2;3;4"), 10)

    def test_add_with_negative_numbers(self):
        """
        Test that the add function raises an exception when negative numbers are provided
        """
        with self.assertRaises(ValueError):
            add("1,-2,3,-4")

if __name__ == '__main__':
    unittest.main()