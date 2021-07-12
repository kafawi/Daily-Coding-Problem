import json


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


def _node2dict(node: Node) -> dict:
    if node is None:
        return None
    return {"val": node.val, "left": _node2dict(node.left), "right": _node2dict(node.right)}


def serialize(root: Node) -> str:
    """Convert the binary tree into a json string


    >>> serialize(Node("A", None, Node("", Node(None,None,None), None)))
    '{"val": "A", "left": null, "right": {"val": "", "left": {"val": null, "left": null, "right": null}, "right": null}}'
    """
    if not root:
        return None
    return json.dumps(_node2dict(root))


def _dict2node(dic: dict):
    if dic is None: return None
    val = dic.get("val")
    left = _dict2node(dic.get("left"))
    right = _dict2node(dic.get("right"))
    return Node(val, left, right)


def deserialize(s: str) -> Node:
    """Parse the serialized json string to a binary tree

    >>> deserialize('{"val": "A", "left": null, "right": {"val": "", "left": {"val": null, "left": null, "right": null}, "right": null}}') == Node("A", None, Node("", Node(None,None,None), None))
    True
    """
    return _dict2node(json.loads(s))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
