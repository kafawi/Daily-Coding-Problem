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
    S = sorted(numbers)

    def _find_subset_for_sum(upper_bound: int, k: int) -> [int]:
        if upper_bound == 0 or S[0] > k:
            return None

        i = _find_rightmost_leq(S, upper_bound, k)
        if S[i] == k:
            return [S[i]]

        for j in range(i, -1, -1):
            subS = _find_subset_for_sum(j, k - S[j])
            if subS:
                return [S[j]] + subS
        return None

    return _find_subset_for_sum(len(S), sum_k)


def _find_rightmost_leq(arr, upper_bound, T) -> int:
    r = upper_bound - 1
    if arr[r] <= T:
        return r
    l = 0
    while(l <= r):
        m = (l+r) // 2
        if arr[m] <= T:
            l = m + 1
        else:  # if arr[m] > T:
            r = m - 1
    return r


if __name__ == '__main__':
    import doctest
    doctest.testmod()
