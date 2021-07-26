"""
>>> find_longest_substring_with_at_most_k_distict_chars("abcba", 2)
'bcb'

>>> find_longest_substring_with_at_most_k_distict_chars("aaaaabcccaa", 1)
'aaaaa'

>>> find_longest_substring_with_at_most_k_distict_chars("aaaaabcccaa", 3)
'aaaaabcccaa'


some edge cases
>>> find_longest_substring_with_at_most_k_distict_chars("abcba", 1)
'a'

>>> find_longest_substring_with_at_most_k_distict_chars("abcba", 0)
''

>>> find_longest_substring_with_at_most_k_distict_chars("abcba", -1)
''

>>> find_longest_substring_with_at_most_k_distict_chars("", 2)
''

>>> find_longest_substring_with_at_most_k_distict_chars(None, 2) == None
True
"""

def find_longest_substring_with_at_most_k_distict_chars(s: str, k: int) -> str:
    if k <= 0:
        return ""
    if s is None:
        return None
    if k >= len(s):
        return s

    char2lastposition = dict()
    longest = ""
    substringstart = 0;
    for pos,ch in enumerate(s):
        if ch not in char2lastposition:
            if len(char2lastposition) == k:
                if len(longest) < pos - substringstart:
                    longest = s[substringstart: pos]
                drop_last_position, drop_char = __get_minimum_char(char2lastposition)  
                substringstart = drop_last_position + 1
                char2lastposition.pop(drop_char)
        char2lastposition[ch] = pos
    if len(longest) < len(s) - substringstart:
        longest = s[substringstart:]
    return longest

def __get_minimum_char(m) -> str:
    min_val = float('inf')
    min_char = None
    for ch, val in m.items():
        if min_val > val:
           min_char = ch
           min_val = val
    return min_val, min_char


if __name__ == "__main__":
    import doctest
    doctest.testmod()