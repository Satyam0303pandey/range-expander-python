# test_range_expander.py

import unittest
from range_expander import expand_range

class TestStage1To3(unittest.TestCase):

    def test_basic_range_expansion(self):
        self.assertEqual(expand_range("1-3,5,7-9"), [1, 2, 3, 5, 7, 8, 9])

    def test_whitespace_and_empty_parts(self):
        self.assertEqual(expand_range(" , 1 - 3 , , 5 "), [1, 2, 3, 5])
        self.assertEqual(expand_range(" , , , 7 "), [7])
        self.assertEqual(expand_range("4-4, , 6 "), [4, 6])
    
    def test_custom_delimiters(self):
        self.assertEqual(expand_range("1..3, 5"), [1, 2, 3, 5])
        self.assertEqual(expand_range("10 to 12,15"), [10, 11, 12, 15])
        self.assertEqual(expand_range("4~6"), [4, 5, 6])

if __name__ == '__main__':
    unittest.main()
