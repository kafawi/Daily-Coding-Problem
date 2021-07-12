import re


class Node:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        val_test = self.val == other.val
        left_test = self.left == other.left
        right_test = self.right == other.right
        return val_test and left_test and right_test


def serialize(root: Node) -> str:
    """Convert the binary tree into a string

     Representation looks like:
     ("<val:String>";<left:Node>;<right:Node>)

     >>> serialize(Node("A", None, Node("", Node(None,None,None), None))) == '("A";;("";(;;);))'
     True
     """
    if not root: return ''
    val_str = '' if root.val is None else '"{}"'.format(root.val)
    return '({};{};{})'.format(val_str, serialize(root.left), serialize(root.right))


def deserialize(s: str) -> Node:
    """Parse the serialized string to a binary tree
  
    Input should be in the following format else Error
    ("<val:String>";<left:Node>;<right:Node>)

    >>> deserialize('("A";;("";(;;);))') == Node("A", None, Node("", Node(None,None,None), None))
    True
    """
    if s is None: raise ValueError("Cannot operate on a None")

    pattern = r'^\(("[^"]*")?;(\(.*\))?;(\(.*\))?\)$'
    s = s.strip()
    match = re.match(pattern, s)
    if not match: raise ValueError("The Node has an incorrect Format and does not match")
    if len(match.group(0)) == 0: return None

    val = None if not match.group(1) else match.group(1)[1:-1]
    left = None if not match.group(2) else deserialize(match.group(2))
    right = None if not match.group(3) else deserialize(match.group(3))
    return Node(val, left, right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n = deserialize('("A";;("";(;;);))')
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
