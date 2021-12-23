import unittest
from solution import justify

class TestJustify(unittest.TestCase):
    
    text_fox = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    
    def _test_k_fox(self, k, expected):
        self.assertEquals(justify(self.text_fox, k), expected)
    
    def test_min_5(self):
        expected = [
            "the  ",
            "quick",
            "brown",
            "fox  ",
            "jumps",
            "over ",
            "the  ",
            "lazy ",
            "dog  "
        ]
        self.assertEquals(justify(self.text_fox, 5), expected)
    
    def test_k_16(self):
        expected =["the  quick brown", # 1 extra space on the left
                   "fox  jumps  over", # 2 extra spaces distributed evenly
                   "the   lazy   dog"] # 4 extra spaces distributed evenly
        self.assertEquals(justify(self.text_fox, 16), expected)
        
    def test_perfect_line_fit(self):
        expected =["the quick brown fox jumps over the lazy dog"]
        self.assertEquals(justify(self.text_fox, len(expected[0])), expected)
    
    
    def test_one_word(self):
        text = "oneword"
        self.assertEquals(justify([text], len(text)), [text])
        self.assertEquals(justify([text], len(text)+1), [text + " "])
        self.assertEquals(justify([text], len(text)+2), [text + "  "])


if __name__ == "__main__":
    unittest.main()
