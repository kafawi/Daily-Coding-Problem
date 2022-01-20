"""Tests
    >>> find_longest_palindromic_substring("aabcdcb")
    'bcdcb'
    >>> find_longest_palindromic_substring("bananas")
    'anana'
"""


def find_longest_palindromic_substring(s: str) -> str:
    def _is_palindrom(from_: int, to: int) -> bool:
        return s[from_: to] == s[to-1: from_-1 if from_ > 0 else None: -1]

    def _find_longest_palindromic_substring(from_, to) -> tuple[int, int]:
        if _is_palindrom(from_, to):
            return from_, to

        ubfrom, ubto = _find_longest_palindromic_substring(from_+1, to)
        sufrom, suto = _find_longest_palindromic_substring(from_, to-1)

        return (ubfrom, ubto) if ubto-ubfrom > suto-sufrom else (sufrom, suto)

    from_, to = _find_longest_palindromic_substring(0, len(s))
    return s[from_: to]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
