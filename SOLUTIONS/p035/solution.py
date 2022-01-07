"""Tests

    >>> arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    >>> sort_rgb(arr)
    >>> print(arr)
    ['R', 'R', 'R', 'G', 'G', 'B', 'B']
    
    >>> arr = ['R', 'B', 'G']
    >>> sort_rgb(arr)
    >>> print(arr)
    ['R', 'G', 'B']
"""

from typing import List


def sort_rgb(arr: List[str]):
    offset = _sort_key(arr, 'R', 0)
    _sort_key(arr, 'G', offset)


def _sort_key(arr, key, offset):
    i = offset
    j = len(arr) - 1
    while i < j:
        if arr[i] == key:
            i += 1
        elif arr[j] != key:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    return i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
