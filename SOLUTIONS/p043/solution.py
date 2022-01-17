"""Tests

    >>> stack = Stack()
    >>> stack.pop()
    Traceback (most recent call last):
    Stack.EmptyStackError: pop is not allowed on an empty Stack
    
    >>> stack.max()
    Traceback (most recent call last):
    Stack.EmptyStackError: max is not allowed on an empty Stack
    
    >>> for i in [1,2,3,2,4,2]: 
    ...   stack.push(i)
    ...   print(stack.max())
    1
    2
    3
    3
    4
    4
    >>> for _ in range(5): 
    ...   print(stack.pop(), stack.max())
    2 4
    4 3
    2 3
    3 2
    2 1
    
    >>> stack.pop()
    1
    
    >>> stack.max()
    Traceback (most recent call last):
    Stack.EmptyStackError: max is not allowed on an empty Stack
    
    >>> stack.pop()
    Traceback (most recent call last):
    Stack.EmptyStackError: pop is not allowed on an empty Stack

"""


class Stack:
    class EmptyStackError(LookupError):

        def __init__(self, operation="operation"):
            self.message = " ".join(
                [operation, "is not allowed on an empty Stack"])
            super().__init__(self.message)

    class _Node(object):

        __slots__ = ('val', 'prev')

        def __init__(self, _val, _prev=None):
            self.val = _val
            self.prev = _prev

    __slots__ = ('top', 'max_top')

    def __init__(self):
        self.top = None
        self.max_top = None

    def push(self, val):
        self.top = self._Node(val, self.top)
        if not self.max_top or self.max_top.val.val < val:
            self.max_top = self._Node(self.top, self.max_top)

    def pop(self):
        if not self.top:
            raise self.EmptyStackError('pop')
        if self.top == self.max_top.val:
            # pop max list
            max_node = self.max_top
            self.max_top = max_node.prev
            del max_node
        node = self.top
        # pop val list
        self.top = node.prev
        val = node.val
        del node
        return val

    def max(self):
        if not self.max_top:
            raise self.EmptyStackError('max')
        return self.max_top.val.val


if __name__ == '__main__':
    import doctest
    doctest.testmod()
