"""Tests

    >>> find_2nd_largest_node(None)
    Traceback (most recent call last):
    AssertionError
    
    >>> find_2nd_largest_node(Node(0, None, None)) == None
    True
    
    >>> find_2nd_largest_node(Node(0, None, Node(1, None, None)))
    Node(value=0, left=None, right=Node(value=1, left=None, right=None))
    
    >>> find_2nd_largest_node(Node(1, Node(0, None, None), None))
    Node(value=0, left=None, right=None)
    
    >>> tree = Node(4,\
        Node(2, Node(0, None, None), Node(1, None, None)), \
        Node(6, Node(5, None, None), Node(7, None, None))  \
        )
    >>> find_2nd_largest_node(tree).value
    6
    
    >>> tree = Node(0, None, \
        Node(1, None, \
            Node(2, None, \
                Node(6, \
                    Node(4, None, \
                        Node(5, None, None) \
                    ), None ))))
    >>> find_2nd_largest_node(tree).value
    5
"""
from collections import namedtuple

Node = namedtuple('Node', ['value', 'left', 'right'])


def find_2nd_largest_node(root: Node) -> Node:
    assert root

    parent = None
    largest = root
    while largest.right:
        parent = largest
        largest = largest.right

    if not largest.left:
        return parent

    second_largest = largest.left
    while second_largest.right:
        second_largest = second_largest.right
    return second_largest


if __name__ == '__main__':
    import doctest
    doctest.testmod()
