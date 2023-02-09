"""Test
    >>> q = Queue()
    >>> q.enqueue('a')
    >>> q.enqueue('b')
    >>> q.enqueue('c')
    >>> out = [q.dequeue()]
    >>> out += [q.dequeue()]
    >>> out += [q.dequeue()]
    >>> out
    ['a', 'b', 'c']
    
    >>> q = Queue()
    >>> q.dequeue()
    Traceback (most recent call last):
     ...
    EOQError
"""
from typing import Any


class Stack:
    __slots__ = ('_elements')

    def __init__(self):
        self._elements = []

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def push(self, element: Any):
        self._elements.append(element)

    def pop(self) -> Any:
        return self._elements.pop()


class EOQError(Exception):
    """Dequeue beyond end of queue.
    """


class Queue:
    __slots__ = ('_in', '_out')

    def __init__(self):
        self._in = Stack()
        self._out = Stack()

    @staticmethod
    def _flip(_from: Stack, _to: Stack):
        while not _from.is_empty():
            _to.push(_from.pop())

    def enqueue(self, element: Any):
        if not self._out.is_empty():
            self._flip(self._out, self._in)
        self._in.push(element)

    def dequeue(self) -> Any:
        if not self._in.is_empty():
            self._flip(self._in, self._out)
        if self._out.is_empty():
            raise EOQError()
        return self._out.pop()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
