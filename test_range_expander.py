import unittest
from range_expander import expand_range

class TestStage1(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(expand_range("1-3,5,7-9"), [1, 2, 3, 5, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
# test_range_expander.py

import unittest
from range_expander import expand_range

# ✅ Test class name — can remain same or updated
class TestStage1And2(unittest.TestCase):
    
    # ✅ Existing test from Stage 1
    def test_basic_range_expansion(self):
        self.assertEqual(expand_range("1-3,5,7-9"), [1, 2, 3, 5, 7, 8, 9])
    
    # ✅ New test for Stage 2
    def test_whitespace_and_empty_parts(self):
        self.assertEqual(expand_range(" , 1 - 3 , , 5 "), [1, 2, 3, 5])
        self.assertEqual(expand_range(" , , , 7 "), [7])
        self.assertEqual(expand_range("4-4, , 6 "), [4, 6])

# ✅ Boilerplate to run the test file
if __name__ == '__main__':
    unittest.main()
