"""Test
    >>> BIG = 10**6
    >>> counts = [0]*7
    >>> for _ in range(7*BIG):
    ...     counts[rand7()-1] += 1
    >>> rel_errs = [n/BIG-1 for n in counts]
    >>> all([err < 0.005 for err in rel_errs])
    True

"""
from random import randint


def rand5():
    return randint(1, 5)


def rand7():
    n = float('inf')
    while(n >= 21):
        n = 5*(rand5()-1) + (rand5()-1)
    return n % 7 + 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
