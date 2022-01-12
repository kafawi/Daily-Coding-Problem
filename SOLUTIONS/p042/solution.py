"""Test

    >>> sorted(find_subset_for_sum([12, 1, 61, 5, 9, 2], 24))
    [1, 2, 9, 12]
    
    >>> find_subset_for_sum([12, 1, 61, 5, 9, 2], 1)
    [1]
    
    >>> find_subset_for_sum([12, 1, 61, 5, 9, 2], 61)
    [61]
    
    >>> find_subset_for_sum([12, 11, 10, 14], 1) == None
    True
    
    >>> sorted(find_subset_for_sum([], 1))
    Traceback (most recent call last):
    AssertionError

"""


def find_subset_for_sum(numbers: list[int], sum_k: int) -> list[int] | None:
    assert numbers and min(numbers) > 0
    sorted_S = sorted(numbers)
    return _find_subset_for_sum(sorted_S, sum_k)


def _find_subset_for_sum(S: list[int], k: int) -> list[int] | None:
    if not S:
        return None
    i = len(S)-1
    while(i > 0 and S[i] > k):
        i -= 1
    if S[i] == k:
        return [k]

    for j in range(i, -1, -1):
        subS = _find_subset_for_sum(S[:j], k - S[j])
        if subS:
            return [S[j]] + subS
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
