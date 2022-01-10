"""Tests

    >>> calculate_number_of_queen_arrangement(1)
    1
    >>> calculate_number_of_queen_arrangement(2)
    0
    >>> calculate_number_of_queen_arrangement(3)
    0
    >>> calculate_number_of_queen_arrangement(4)
    2
    >>> calculate_number_of_queen_arrangement(5)
    10
    >>> calculate_number_of_queen_arrangement(6)
    4
    >>> calculate_number_of_queen_arrangement(7)
    40
"""
from typing import List


def calculate_number_of_queen_arrangement(N: int) -> int:
    queen_y2x = [-1]*N
    return _calc_num_of_queen_arrangements_recur(N, 0, queen_y2x)


def _calc_num_of_queen_arrangements_recur(N: int, y: int, queen_y2x: List[int]) -> int:
    if y == N:
        return 1

    arrangements = 0
    for x in _free_x(N, y, queen_y2x):
        queen_y2x[y] = x
        arrangements += _calc_num_of_queen_arrangements_recur(
            N, y+1, queen_y2x)
    return arrangements


def _free_x(N: int, Y: int, queen_y2x: List[int]):
    """Getting free cells in the Yth board row

       >>> [x for x in _free_x(1, 0,[-1])]
       [0]

       >>> [x for x in _free_x(2, 1,[ 0,-1])]
       []
       >>> [x for x in _free_x(2, 0,[-1,-1])]
       [0, 1]

       >>> [x for x in _free_x(3, 0,[ -1 ,-1, -1])]
       [0, 1, 2]
       >>> [x for x in _free_x(3, 1,[0,-1,-1])]
       [2]
       >>> [x for x in _free_x(3, 2,[0,2,-1])]
       []


       >>> [x for x in _free_x(4, 0,[ -1 ,-1, -1, -1])]
       [0, 1, 2, 3]
       >>> [x for x in _free_x(4, 1,[0, -1, -1, -1])]
       [2, 3]
       >>> [x for x in _free_x(4, 1,[1, -1, -1, -1])]
       [3]
       >>> [x for x in _free_x(4, 1,[2, -1, -1, -1])]
       [0]
       >>> [x for x in _free_x(4, 1,[3, -1, -1, -1])]
       [0, 1]

       >>> [x for x in _free_x(4, 2,[0, 2, -1, -1])]
       []
       >>> [x for x in _free_x(4, 2,[0, 3, -1, -1])]
       [1]
       >>> [x for x in _free_x(4, 3,[0, 3, 2, -1])]
       []
    """
    x_occupie_count = [0]*N
    for y, x in enumerate(queen_y2x[:Y]):
        # vertical
        x_occupie_count[x] += 1
        # diagonal
        dx = Y-y
        if x-dx >= 0:
            x_occupie_count[x-dx] += 1
        if x+dx < N:
            x_occupie_count[x+dx] += 1

    for x, count in enumerate(x_occupie_count):
        if count == 0:
            yield x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
