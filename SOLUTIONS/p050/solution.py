"""Test
    0 = 0
    >>> eval(Node(0))
    0
    
    42 = 42
    >>> eval(Node(42))
    42
    
    -11 = -11
    >>> eval(Node(-11))
    -11
    
    1+2 = 3
    >>> eval(Node('+',Node(1),Node(2))) 
    3
    
    1+-2
    >>> eval(Node('+',Node(1), Node(-2)))
    -1
    
    3-7 = -4
    >>> eval(Node('-',Node(3),Node(7)))
    -4
    
    -3*7 = 21
    >>> eval(Node('*',Node(-3),Node(7)))
    -21
    
    66/6 = 11
    >>> eval(Node('/',Node(66),Node(6)))
    11
    
    7/2 = 3
    >>> eval(Node('/',Node(7),Node(2)))
    3
    
    (3 + 2) * (4 + 5) = 45
    >>> tree = Node('*',
    ...   Node('+', Node(3), Node(2)),
    ...   Node('+', Node(4), Node(5))
    ... )
    >>> eval(tree)
    45
"""
from enum import Enum


class Operation(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DEVISION = 4

    @classmethod
    def parse(cls, symbol):
        return {"+": cls.ADDITION,
                "-": cls.SUBTRACTION,
                "*": cls.MULTIPLICATION,
                "/": cls.DEVISION
                }[symbol]

    @classmethod
    def call(cls, operation):
        return {cls.ADDITION: int.__add__,
                cls.SUBTRACTION: int.__sub__,
                cls.MULTIPLICATION: int.__mul__,
                cls.DEVISION: int.__floordiv__}[operation]


class Node:
    __slots__ = ('operant_left', 'operant_right', 'value')

    def __init__(self, value, left=None, right=None):
        self.value = Operation.parse(value) if isinstance(
            value, str) and value in "+-*/" else value
        self.operant_left = left
        self.operant_right = right


def eval(term):
    if isinstance(term.value, int):
        return term.value
    # elif isinstance(term.value, Enum) and term.value in Operation:
    op1 = eval(term.operant_left)
    op2 = eval(term.operant_right)
    return Operation.call(term.value)(op1, op2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
