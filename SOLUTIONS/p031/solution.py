def compute_edit_distance(s: str, t: str) -> int:
    """Compute the Levenshtein distance

    >>> compute_edit_distance("", "abc")
    3
    >>> compute_edit_distance("abc", "")
    3
    >>> compute_edit_distance("bc", "abc")
    1
    >>> compute_edit_distance("abc", "bc")
    1
    >>> compute_edit_distance("ac", "abc")
    1
    >>> compute_edit_distance("abc", "ac")
    1
    >>> compute_edit_distance("ab", "abc")
    1
    >>> compute_edit_distance("abc", "ab")
    1
    >>> compute_edit_distance("kitten", "sitting")
    3
    >>> compute_edit_distance("sitting", "kitten")
    3
    """
    d = list(range(len(s)+1))
    prev_d = [0]*(len(s)+1)
    for j, tchar in enumerate(t, 1):
        prev_d, d = d, prev_d
        d[0] = j
        for i, schar in enumerate(s, 1):
            deletion = d[i-1] + 1
            insertion = prev_d[i] + 1
            substitution = prev_d[i-1] + (0 if schar == tchar else 1)
            d[i] = min(deletion, insertion, substitution)
    return d[len(s)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
