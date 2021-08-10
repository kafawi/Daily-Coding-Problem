from typing import Optional, List, Any
from types import FunctionType

class Node:
    
    def __init__(self, value :Optional):
        self._value :Any = value
        self._is_locked :bool = False
        self._is_any_descendant_locked :bool = False
        self._parent :Optional['Node']= None
        self._left :Optional['Node']= None
        self._right :Optional['Node']= None

    def is_locked(self):
        return self._is_locked

    def _is_any_ancestor_locked(self) -> bool:
        tmp :Node = self._parent
        while tmp:
            if tmp.is_locked(): 
                return True
            tmp = tmp._parent
        return False

    @property
    def _sibling(self) -> Optional['Node']:
        if self._parent:
            if self._parent._left is self: 
                return self._parent._right
            else:
                return self._parent._left
        return None
    
    def lock(self) -> bool:
        if self._is_locked:
            return True
        if self._is_any_descendant_locked or self._is_any_ancestor_locked():
            return False
        tmp = self._parent
        while tmp and not tmp._is_any_descendant_locked:
            tmp._is_any_descendant_locked = True
            tmp = tmp._parent
        self._is_locked = True
        return True
    
    def unlock(self) -> bool:
        if not self._is_locked:
            return True
        if self._is_any_descendant_locked or self._is_any_ancestor_locked():
            return False
        tmp = self
        while tmp._parent and (not tmp._sibling or not tmp._sibling._is_any_descendant_locked):
            tmp._parent._is_any_descendant_locked = False
            tmp = tmp._parent
        self._is_locked = False
        return True

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: Any):
        if not self._is_locked:
            self._value = value
    
    @staticmethod
    def create_tree(values: List) -> Optional['Node']:
        """Create a compact packed binary tree from root to leaves.

        in order of the values in the list
        """
        if not values: return None
        nodes :List[Node] = [None] + [Node(value) for value in values]
        for n, node in enumerate(nodes):
            if n == 0: continue
            if n != 1: node._parent = nodes[n//2]
            node._left = nodes[2*n] if 2*n < len(nodes) else None
            node._right = nodes[2*n+1] if 2*n+1 < len(nodes) else None
        return nodes[1]

    def __repr__(self):
        return "{}:{}:{}:({},{})".format(
            self._value,
            "x" if self._is_locked else "o",
            "x" if self._is_any_descendant_locked else "o",
            self._left if self._left else '-',
            self._right if self._right else '-'
        )
    

import unittest

class TestNode(unittest.TestCase):

    def assert_node_equal(self, node :Node, **attr2value):
        for attr, value in attr2value.items():
            if attr in dir(node):
                self.assertEqual(value, getattr(node, attr))
    
    def assert_tree_preorder_equal(self, root :Node, expacted_preorder_nodes: List[dict]):
        attr2value = expacted_preorder_nodes.pop(0)
        self.assert_node_equal(root, **attr2value)
        if root._left:
            self.assert_tree_preorder_equal(root._left, expacted_preorder_nodes)
        if root._right:
            self.assert_tree_preorder_equal(root._right, expacted_preorder_nodes)

    def test_create_tree(self):
        values = [0,1,2,3,4,5,6,7,8,9]
        root = Node.create_tree(values)
        preorder_values = [0,1,3,7,8,4,9,2,5,6]
        expacted_preorder_nodes = [{'_value': value, '_is_locked': False, '_is_any_descendant_locked': False} for value in preorder_values]
        self.assert_tree_preorder_equal(root, expacted_preorder_nodes)
    
    def test_is_locked(self):
        node = Node(0)
        self.assertFalse(node.is_locked())
        node.lock()
        self.assertTrue(node.is_locked())
        node.unlock()
        self.assertFalse(node.is_locked())

    def test_lock(self):
        root = Node.create_tree([0,1,2])
        self.assertTrue(root.lock()) 
        self.assertTrue(root.is_locked())

        self.assertFalse(root._left.lock())
        self.assertFalse(root._left.is_locked())
        self.assertFalse(root._right.lock())
        self.assertFalse(root._right.is_locked())

        root = Node.create_tree([0,1,2,3,4,5,6,7])
        self.assertTrue(root._left.lock())
        self.assertTrue(root._left.is_locked()) 

        self.assertFalse(root.lock())

        self.assertFalse(root._left._right.lock())
        self.assertFalse(root._left._left.lock())

        self.assertTrue(root._right._left.lock())
        self.assertTrue(root._right._left.is_locked())

        self.assertFalse(root._right.lock())
        self.assertFalse(root.lock())

        self.assertTrue(root._right._right.lock())
        self.assertTrue(root._right._right.is_locked())


    def test_unlock(self):
        root = Node.create_tree([0,1,2])
        root.lock() 
        self.assertTrue(root.is_locked())
        # already unlocked node is always true in my interpretation of the problem
        self.assertTrue(root._left.unlock()) 
        self.assertTrue(root.unlock())
        self.assertFalse(root.is_locked())

        root = Node.create_tree([0,1,2,3,4,5,6,7])
        root._left.lock()
        root._right._left.lock()
        root._right._right.lock()
        
        self.assertTrue(root._right._left.unlock())
        self.assertTrue(root._left.unlock())
        self.assertTrue(root._right._right.unlock())


if __name__ == "__main__":
    unittest.main()