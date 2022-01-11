"""Tests

    >>> find_non_duplicated([6, 1, 3, 3, 3, 6, 6])
    1
    >>> find_non_duplicated([13, 19, 13, 13])
    19
    >>> find_non_duplicated([11, -13, -3, 11, -13, -13, 11])
    -3
"""
from typing import List


def find_non_duplicated(array: List[int], N: int = 3) -> int:
    """Find the only non N times duplicate in an array 

    Args:
        array (List[int]): integer where one is not a duplicate
        N (int, optional): number of duplications Defaults to 3.

    Returns:
        int: the non duplicate

    >>> find_non_duplicated([13, 19, 13, 13], N=3)
    19
    >>> find_non_duplicated([13, 19, 13, 13, 44, 13, 44], N=2)
    19
    """
    assert array
    msb = find_msb(array)
    non_duplicate = 0
    for n in range(msb+1):
        bit = 1 << n
        cnt_bit = sum(bool(bit & value) for value in array)
        if cnt_bit % N:
            non_duplicate |= bit

    def twos_complement(x): return -((x-1) ^ ((1 << (msb+1))-1))
    return twos_complement(non_duplicate) if non_duplicate & (1 << msb) else non_duplicate


def find_msb(array: List[int]) -> int:
    """Find the greates MSB of all numbers in array

    Args:
        array (List[int]): integers

    Returns:
        int: greates MSB postion

    >>> find_msb([])
    -1
    >>> find_msb([0])
    -1
    >>> find_msb([-1])
    1
    >>> find_msb([1])
    1
    >>> find_msb([1,2,3,4,5]) # 5 -> 4 +1 = 0b0101 -> 2 + sign bit
    3
    >>> find_msb([8,9,3,5]) # 9 -> 8 + 1 = 0b01001 -> 3 + sign bit
    4
    >>> find_msb([3,6,-9,5]) # -9 -> 3 + sign bit
    4
    """
    from math import log
    def to_msb(x): return int(log(abs(x), 2)) + 1  # + sign bit
    return max([-1] + [to_msb(n) for n in array if n])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
