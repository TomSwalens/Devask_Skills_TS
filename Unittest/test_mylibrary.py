# test_mylibrary.py
import unittest
from mylibrary import add_numbers, multiply_numbers

class TestMyLibrary(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        # Add more test cases for add_numbers if needed

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        # Add more test cases for multiply_numbers if needed

if __name__ == '__main__':
    unittest.main()