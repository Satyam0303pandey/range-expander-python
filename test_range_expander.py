import unittest
from range_expander import expand_range

class TestStage1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(expand_range("1-3,5,7-9"), [1, 2, 3, 5, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
