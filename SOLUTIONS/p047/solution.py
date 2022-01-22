"""Test
    >>> calc_maximum_profit([9, 11, 8, 5, 7, 10])
    5
    
    >>> calc_maximum_profit([3, 1, 0])
    -1
    
    >>> calc_maximum_profit([0, 2, 3])
    3
    
    >>> calc_maximum_profit(None)
    Traceback (most recent call last):
    AssertionError
    
    >>> calc_maximum_profit([])
    Traceback (most recent call last):
    AssertionError

    >>> calc_maximum_profit([1])
    Traceback (most recent call last):
    AssertionError
    
"""


def calc_maximum_profit(stock_price_history: list[int]) -> int:
    assert stock_price_history and len(stock_price_history) > 2
    maximum_profit = -float('inf')
    minimum_price = stock_price_history[0]
    for price in stock_price_history[1:]:
        maximum_profit = max(maximum_profit, price - minimum_price)
        minimum_price = min(minimum_price, price)
    return maximum_profit


if __name__ == "__main__":
    import doctest
    doctest.testmod()
