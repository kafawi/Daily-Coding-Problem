"""Test
Testcase leaf
>>> count_unival_trees(Node(0,None, None))
1

Testcases simple trees
>>> count_unival_trees(Node(0,Node(1,None,None), None))
1
>>> count_unival_trees(Node(1,None, Node(1,None,None)))
2
>>> count_unival_trees(Node(1,Node(0,None,None), Node(1,None,None)))
2
>>> count_unival_trees(Node(0,Node(0,None,None), Node(0,None,None)))
3

Testcase example
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

>>> count_unival_trees(Node(0, Node(1, None, None), Node(0, Node(1, Node(1, None, None), Node(1, None, None)), Node(0,None,None))))
5
"""


class Node:
    def __init__(self, value, left, right):
        self.value_ = value;
        self.left_ = left
        self.right_ = right


def __count_unival_trees(root: Node) -> (int, bool):
  count, is_unival = 0, True
  if root.left_:
    count_left, is_left_unival = __count_unival_trees(root.left_)
    is_unival &= is_left_unival and root.value_ == root.left_.value_
    count += count_left
  if root.right_:
    count_right, is_right_unival = __count_unival_trees(root.right_)
    is_unival &= is_right_unival and root.value_ == root.right_.value_
    count += count_right

  if is_unival: 
    count += 1
  return count, is_unival


def count_unival_trees(root: Node) -> int:
  return __count_unival_trees(root)[0]


if __name__ == '__main__':
  import doctest
  doctest.testmod()
