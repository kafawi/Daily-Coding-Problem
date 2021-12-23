"""
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

>>> encode("AAAABBBCCDAA")
'4A3B2C1D2A'

>>> decode("4A3B2C1D2A")
'AAAABBBCCDAA'
"""

def encode(text :str) -> str:
    """run-length encoding
    
    >>> encode("")
    ''
    
    >>> encode("abc")
    '1a1b1c'
    
    just for fun
    >>> encode("122333444455555")
    '1122334455'
    """
    if text == "": return ""
    s = ""
    char = text[0]
    count = 1
    for c in text[1:]:
        if char != c:
            s += str(count) + char
            char = c
            count = 1
        else:
            count += 1
    s += str(count) + char
    return s
   
def decode(text :str) -> str:
    """run-length decoding
    
    >>> decode("")
    ''
    
    >>> decode("1a1b1c")
    'abc'
    
    just for fun
    >>> decode("1122334455")
    '122333444455555'
    """
    return "".join(text[i+1] * int(text[i]) for i in range(0, len(text), 2)) 

if __name__=='__main__':
    import doctest
    doctest.testmod()
  