"""Test
    >>> cards = ['A', 'B', 'C', 'D']
    >>> copy_cards = cards.copy()
    >>> shuffle(cards)
    >>> success = True
    >>> for card in copy_cards:
    ...    if not card in cards:
    ...        print(card)
    ...        success = False
    >>> if success: print('Success')
    Success
"""
from typing import List, Any
from random import randint


def rand_int(k: int) -> int:
    return randint(1, k)


def shuffle(array: List[Any]):
    for i in range(len(array)-1, 0, -1):
        picked_card_index = rand_int(i)
        array[i], array[picked_card_index] = array[picked_card_index], array[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
