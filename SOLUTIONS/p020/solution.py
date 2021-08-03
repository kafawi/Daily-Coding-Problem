from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Node:
    val :Any
    next :Optional['Node'] = None


@dataclass
class List:
    first :Optional[Node] 


def retrieve_length(list :List) -> int:
    tmp :Node = list.first
    length :int = 0
    while tmp:
        length+=1
        tmp = tmp.next
    return length 


def find_merging_node(A: List, B: List) -> Optional[Node]:
    N = retrieve_length(A)  # N 
    M = retrieve_length(B)  # M

    shorter :Node = A.first if N < M else B.first
    longer :Node = B.first if N < M else A.first

    # running to get longer to the same length of shorter
    for _ in range(abs(N - M)):
       longer = longer.next
    
    while shorter and longer is not shorter:
        longer = longer.next
        shorter = shorter.next
  
    return shorter


import unittest

class TestFindMergeNode(unittest.TestCase):

    def test_retrieve_length(self):
        l_empty :List = List(None)
        self.assertEqual(retrieve_length(l_empty), 0)
        l_full :List = List(Node( 3, Node(7)))
        self.assertEqual(retrieve_length(l_full), 2)

    def test_in_the_middle_same_length(self):
        merge :Node= Node(8, Node(10))
        A :List = List(Node( 3, Node(7, merge)))
        B :List = List(Node(99, Node(1, merge)))
        self.assertEqual(find_merging_node(A, B), merge)

    def test_in_the_middle_different_length(self):
        merge :Node= Node(8, Node(10))
        A :List = List(Node( 3, Node(7, merge)))
        B :List = List(Node(100,Node(99, Node(1, merge))))
        C :List = List(merge)
        self.assertEqual(find_merging_node(A, B), merge)
        self.assertEqual(find_merging_node(A, C), merge)
        self.assertEqual(find_merging_node(C, B), merge)

    def test_first_node_both(self):
        merge :Node= Node(8, Node(10))
        A :List = List(merge)
        B :List = List(merge)
        self.assertEqual(find_merging_node(A, B), merge)

    def test_last_node(self):
        merge :Node= Node(8)
        A :List = List(Node('a0',Node('a1', merge)))
        B :List = List(Node('b0',Node('b1', Node('b2', merge))))
        self.assertEqual(find_merging_node(A, B), merge)

    def test_nowhere_empty(self):
        A :List = List(None)
        B :List = List(Node('b0',Node('b1', Node('b2'))))
        C :List = List(None)
        self.assertEqual(find_merging_node(A, C), None)
    
    def test_nowhere_empty_both(self):
        A :List = List(None)
        B :List = List(Node('b0',Node('b1', Node('b2'))))
        self.assertEqual(find_merging_node(A, B), None)

    def test_nowhere_both_filled(self):
        A :List = List(Node('a0',Node('a1')))
        B :List = List(Node('b0',Node('b1', Node('b2'))))
        self.assertEqual(find_merging_node(A, B), None)


if __name__ == "__main__":
    unittest.main()
