import unittest
from solution import are_brackets_balanced

class TestAreBracketsBalanced(unittest.TestCase):
    
    def _loop_true(self, *inputs):
        for i in inputs:
            self.assertTrue(are_brackets_balanced(i))
    
    def _loop_false(self, *inputs):
        for i in inputs:
            self.assertFalse(are_brackets_balanced(i))
    
    def test_empty(self):
        self.assertTrue(are_brackets_balanced(""))
    
    def test_pairs(self):
        self._loop_true("()", "[]", "{}",
                        "(())", "[[]]","{{}}")
    
    def test_mixed_balanced(self):
        self.assertTrue(are_brackets_balanced("([])[]({})"))
        
    def test_single_openings(self):
        self._loop_false("(", "[", "{")
    
    def test_single_closings(self):
        self._loop_false(")", "]", "}")
    
    def test_wrong_order(self):
        self._loop_false(")(", "][", "}{")
        
    def test_mixed_unbalanced(self):
        self._loop_false("([)]","((()")


if __name__ == "__main__":
    unittest.main()
