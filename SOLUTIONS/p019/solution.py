from math import inf
from typing import List
from numbers import Number

def calc_best_price(price_table: List[List[Number]]) -> int:
    minima = [(0, -1), (0, -1)]
    for n in range(len(price_table)):
        local_minima = [(inf, -1), (inf, -1)]
        for k in range(len(price_table[n])):
            path_sum = price_table[n][k]
            path_sum += minima[0][0] if minima[0][1] != k else minima[1][0]
            if path_sum < local_minima[0][0]:
                local_minima[1], local_minima[0] = local_minima[0], (path_sum, k)
            elif path_sum < local_minima[1][0]:
                local_minima[1] = (path_sum, k)
        minima = local_minima
    return minima[0][0]


import unittest

class TestBoundedOrderLog(unittest.TestCase):

    def test_2n2k(self):
        m = [
            [1, 2],
            [2, 4],
        ]
        self.assertEqual(calc_best_price(m), 2+2)

    def test_concept(self):
        m = [
            [ 1,  2,  3],
            [ 4,  5,  6],
            [ 7,  8,  9],
            [10, 11, 12],
        ]
        self.assertEqual(calc_best_price(m), 24)


if __name__ == "__main__":
    unittest.main()
