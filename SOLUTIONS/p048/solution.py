"""Test

    >>> build_tree(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    >>> build_tree(['a', 'b', 'e', 'c', 'f'], ['b', 'e', 'a', 'f', 'c',])
    ['a', 'b', 'c', None, 'e', 'f', None]
    
"""

import contextlib
from math import log
from array import array


class Tree:
    
    __slots__ = ('__values')
    
    def __repr__(self):
        return repr(self.__values)    
    
    def __init__(self):
        self.__values = []
    
    def __grow(self):
        size = len(self.__values)
        new_size = 2*(size+1) - 1 
        tmp = [None] * new_size
        tmp[:size] = self.__values
        self.__values = tmp
        del tmp
    
    def set_value(self, idx: int, value):
        while len(self.__values)-1 < idx:
            self.__grow()
        self.__values[idx] = value
        
    def get_left(self, root :int) -> int:
        return 2*root + 1
        
    def get_right(self, root :int) -> int:
        return 2*root + 2
        

def build_tree(preorder: list, inorder: list) -> Tree:
    assert len(preorder) == len(inorder), "Argument have to be two lists of same size."
    preorder_it = iter(preorder)
    tree = Tree()

    def _build_tree(node: int, inorder_slice: list):
        nonlocal preorder_it
        value = next(preorder_it) # raise Stopiteration if the iteration is finished
        
        try:
            inorder_idx = inorder_slice.index(value)
        except ValueError:
            assert False, f"preorder value {value} is not found in inorder"
        inorder_left = inorder_slice[:inorder_idx]
        inorder_right = inorder_slice[inorder_idx+1:]

        tree.set_value(node, value)
        if inorder_left: _build_tree(tree.get_left(node), inorder_left)
        if inorder_right: _build_tree(tree.get_right(node), inorder_right)

    with contextlib.suppress(StopIteration):
        _build_tree(0, inorder)
    return tree


if __name__ == '__main__':
    import doctest
    doctest.testmod()
