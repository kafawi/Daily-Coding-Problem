import unittest
from solution import matches

class TestMatchesIter0(unittest.TestCase):

    def test_ideom(self):
        self.assertTrue(matches("42", "42"))

    def test_wrong_order(self):
        self.assertFalse(matches("abc", "acd"))
    
    def test_wrong_size(self):
        self.assertFalse(matches("abc", "abcd"))
        self.assertFalse(matches("abc", "ab"))
    
    def test_empty(self):
        self.assertTrue(matches("", ""))
        # its edges
        self.assertTrue(matches("a", "a"))
        self.assertFalse(matches("a", "b"))


class TestMatchesIter1(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(matches("", "."))

    def test_one_char(self):
        self.assertTrue(matches("a", "."))
        self.assertTrue(matches("b", "."))
    
    def test_one_wildcard(self):
        self.assertTrue(matches("42", ".2"))
        self.assertTrue(matches("abc", "a.c"))
        self.assertTrue(matches("abc", ".bc"))
        self.assertTrue(matches("abc", "ab."))

    def test_correct_width(self):
        self.assertTrue(matches("efg", "..."))

    def test_wrong_order(self):
        self.assertFalse(matches("acb", "a.c"))

    def test_wrong_size(self):
        self.assertFalse(matches("abdc", "a.c"))
        self.assertFalse(matches("ac", "a.c"))


class TestMatchesIter2(unittest.TestCase):

    def test_one_char(self):
        self.assertTrue(matches("", "a*"))
        self.assertTrue(matches("a", "a*"))
        self.assertTrue(matches("aa", "a*"))

    def test_self_consuming(self):
        self.assertTrue(matches("", "a*a*"))
        self.assertTrue(matches("a", "a*a*"))
        self.assertTrue(matches("aa", "a*a*"))
        self.assertTrue(matches("aaa", "a*a*"))

    def test_off_by_one(self):
        self.assertFalse(matches("b", "a*"))
        self.assertFalse(matches("bb", "a*"))
        self.assertFalse(matches("ab", "a*"))
        self.assertFalse(matches("ba", "a*"))

    def test_the_trap(self):
        self.assertFalse(matches("", "a*aa*"))
        self.assertTrue(matches("a",  "a*aa*"))
        self.assertTrue(matches("aa",  "a*aa*"))

    def test_compination_with_previous_iteration(self):
        self.assertTrue(matches("a", "a*.a*"))
        self.assertFalse(matches("", "a*.a*"))
        self.assertTrue(matches("aa", "a*.a*"))
        self.assertTrue(matches("aaa", "a*.a*"))

        self.assertTrue(matches("b", "a*.a*"))
        self.assertTrue(matches("aba", "a*.a*"))

        self.assertTrue(matches("ba", ".a*"))
        self.assertFalse(matches("ab", ".a*"))
        self.assertFalse(matches("ba", "a*."))
        self.assertTrue(matches("ab", "a*."))
    

class TestMatchesIter3(unittest.TestCase):

    def test_one_trumpf(self):
        self.assertTrue(matches("", ".*"))
        self.assertTrue(matches("a", ".*"))
        self.assertTrue(matches("ab", ".*"))

    def test_trumpf_in_different_places(self):
        self.assertTrue(matches("abc", ".*c"))
        self.assertFalse(matches("abc", ".*a"))
        self.assertTrue(matches("abc", "a.*"))
        self.assertFalse(matches("abc", "c.*"))
        self.assertTrue(matches("abcd", "a.*d"))
        self.assertFalse(matches("abcd", "a.*e"))
        self.assertFalse(matches("abcd", "b.*d"))
    
    def test_encapsulation(self):
        self.assertTrue(matches("a", ".*a.*"))
        self.assertTrue(matches("ba", ".*a.*"))
        self.assertTrue(matches("abc", ".*a.*"))
        self.assertTrue(matches("cab", ".*a.*"))

    def test_the_trap(self):
        self.assertTrue(matches("aacac", ".*a.*c"))
        self.assertFalse(matches("aaca", ".*a.*c"))

    def test_all_iter_together(self):
        pattern = ".*<tag id=....> ab*c </tag>.*"
        self.assertTrue(matches("  <tag id=1234> ac </tag>  42", pattern))
        self.assertFalse(matches("  <tag id=1234> ac </taf>  42", pattern))
        self.assertFalse(matches("  <tag id=123> ac </tag>  42", pattern))
        self.assertTrue(matches("  <tag id=1234> abbbbc </tag>  42", pattern))
    
if __name__ == "__main__":
    tests = [
        "TestMatchesIter0",
        "TestMatchesIter1",
        "TestMatchesIter2",
        "TestMatchesIter3",
    ]
    unittest.main(defaultTest=tests)
    
