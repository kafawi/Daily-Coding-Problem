"""Tests
    >>> all(x in [set()] for x in generate_power_set_recur(set()))
    True
    >>> all(x in [set()] for x in generate_power_set_recur(set()))
    True

    >>> all(x in [set(), {1}] for x in generate_power_set_recur({1}))
    True
    >>> all(x in [set(), {1}] for x in generate_power_set_recur({1}))
    True

    >>> all(x in [set(), {1}, {2}, {1, 2}] for x in generate_power_set_recur({1, 2}))
    True
    >>> all(x in [set(), {1}, {2}, {1, 2}] for x in generate_power_set_recur({1, 2}))
    True

    >>> all(x in [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}] for x in generate_power_set_recur({1, 2, 3}))
    True
    >>> all(x in [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}] for x in generate_power_set_bitvec({1, 2, 3}))
    True
"""

from typing import Set, List


def generate_power_set_recur(s: Set[object]) -> List[Set[object]]:
    if not s:
        return [set()]
    elem = s.pop()
    powerset = generate_power_set_recur(s)
    powerset += [subset.union([elem]) for subset in powerset]
    return powerset


def generate_power_set_bitvec(s: Set[object]) -> List[Set[object]]:
    s = list(s)
    powerset = []
    for bitvec in range(2**len(s)):
        subset = {s[j] for j in range(len(s)) if (1 << j) & bitvec}
        powerset += [subset]
    return powerset


if __name__ == "__main__":
    import doctest
    doctest.testmod()
