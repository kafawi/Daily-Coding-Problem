"""Tests

    >>> get_nearest_palindrome('google')
    'elgoogle'
    >>> get_nearest_palindrome('race')
    'ecarace'
    >>> get_nearest_palindrome('bdfeca')
    'abcdefedcba'
    >>> get_nearest_palindrome('racae')
    'eracare'
"""


def get_nearest_palindrome(word: str) -> str:
    if len(word) < 2:
        return word

    first = word[0]
    last = word[-1]

    if first == last:
        return first + get_nearest_palindrome(word[1:-1]) + last
    pal_first = first + get_nearest_palindrome(word[1:]) + first
    pal_last = last + get_nearest_palindrome(word[:-1]) + last
    # check which is lower
    return _get_min_word(pal_first, pal_last)


def _get_min_word(s: str, t: str) -> str:
    if len(s) > len(t):
        return t
    elif len(s) < len(t):
        return s
    else:  # s.length == t.length
        return min(s, t)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
