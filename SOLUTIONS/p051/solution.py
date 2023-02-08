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
    
    >>> permutations = {(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)}
    >>> times = len(permutations)**2
    >>> for _ in range(times):
    ...    cards = [0, 1, 2]
    ...    shuffle(cards)
    ...    shuffled_cards = tuple(cards)
    ...    if shuffled_cards in permutations:
    ...        permutations.remove(shuffled_cards)
    ...    if len(permutations) == 0: 
    ...        break
    >>> print(permutations) # empty set
    set()
"""
from typing import List, Any
from random import randint


def rand_int(k: int) -> int:
    return randint(1, k)


def shuffle(array: List[Any]):
    for i in range(len(array)-1, -1, -1):
        picked_card_index = rand_int(i+1) - 1
        array[i], array[picked_card_index] = array[picked_card_index], array[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
