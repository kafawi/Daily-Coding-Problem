import unittest
from solution import remove_from_back, _get_from_back, Node, SLL

def _string2list(_values :str) -> SLL:
    next_node = None
    head = None
    for value in reversed(_values):
        head = Node(value, next_node)
        next_node = head
    return SLL(head)

def _list2string(_list: SLL) -> str:
    s = ""
    walker = _list.head
    while(walker):
        s += walker.value
        walker = walker.next
    return s


class TestGet(unittest.TestCase):
    
    def _test_helper(self, s, k, c =None):
        l = _string2list(s)
        c = c or s[-1-k] 
        self.assertEqual(_get_from_back(l,k).value, c)
        self.assertEqual(_list2string(l),s)

    def test_middle(self):
        s = "abcdefg"
        for k in range(2,len(s)-2):
            self._test_helper(s, k)

    def test_first(self):
        self._test_helper("abcdefg", 6)
    
    def test_second(self):
        self._test_helper("abcdefg", 5)
        
    def test_second_last(self):
        self._test_helper("abcdefg", 1)
        
    def test_last(self):
        self._test_helper("abcdefg", 0, "g")
        

class TestRemove(unittest.TestCase):
    
    def _test_helper(self, s, k, c=None, after=None):
        l = _string2list(s)
        after = after or s[:-1-k] + s[-k:]
        c = c or s[-1-k] 
        self.assertEqual(remove_from_back(l,k), c) 
        self.assertEqual(_list2string(l),after)

    def test_middle(self):
        s = "abcdefg"
        for k in range(2,len(s)-1-1):
            self._test_helper(s, k)

    def test_first(self):
        self._test_helper("abcdefg", 6, "a", "bcdefg")
    
    def test_second(self):
        self._test_helper("abcdefg", 5, "b", "acdefg")
        
    def test_second_last(self):
        self._test_helper("abcdefg", 1, "f", "abcdeg")
        
    def test_last(self):
        self._test_helper("abcdefg", 0, "g", "abcdef")
    
if __name__ == "__main__":
    tests = [
        "TestGet",
        "TestRemove",
    ]
    unittest.main(defaultTest=tests)
    