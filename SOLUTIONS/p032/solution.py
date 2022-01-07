"""Tests

       >>> good_table = [[1, 1], [1, 1]]
       >>> is_possible_arbitrage([[1, 1], [1, 1]])
       False
       >>> good_table = [[1, 2, 8], [0.5, 1, 4], [0.125, 0.25, 1]]
       >>> is_possible_arbitrage(good_table)
       False

       >>> is_possible_arbitrage([[1, 1], [2, 1]])
       True
       >>> is_possible_arbitrage([[1, 2], [1, 1]])
       True
       >>> is_possible_arbitrage([[1, 2], [2, 1]])
       True

       >>> bad_table = [[1, 2, 4], [0.5, 1, 8], [0.25, 0.125, 1]]
       >>> is_possible_arbitrage(bad_table)
       True
   """
from typing import List
from itertools import permutations


def is_possible_arbitrage(currency_exchange_rates: List[List[float]]) -> bool:
    # init
    n = len(currency_exchange_rates)
    rates = list(currency_exchange_rates[0])

    for _ in range(n - 1):
        for v, w in permutations(range(n), 2):
            if rates[w] != rates[v] * currency_exchange_rates[v][w]:
                return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
