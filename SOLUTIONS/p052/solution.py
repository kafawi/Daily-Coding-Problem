"""Test

    >>> lru = LRUCache(3)
    >>> print(lru.get(0))
    None
    
    >>> lru = LRUCache(3)
    >>> lru.set('a', 39)
    >>> lru.set('b', 40)
    >>> lru.set('c', 41)
    >>> lru.set('d', 42)
    >>> [lru.get('a'), lru.get('b'), lru.get('c'), lru.get('d')]
    [None, 40, 41, 42]
    
    >>> lru = LRUCache(3)
    >>> lru.set('a', 39)
    >>> lru.set('b', 40)
    >>> lru.set('c', 41)
    >>> _ = lru.get('a')
    >>> lru.set('d', 42)
    >>> [lru.get('a'), lru.get('b'), lru.get('c'), lru.get('d')]
    [39, None, 41, 42]
    
    >>> lru = LRUCache(3)
    >>> lru.set('a', 39)
    >>> lru.set('b', 40)
    >>> lru.set('c', 41)
    >>> _ = lru.get('a')
    >>> _ = lru.get('c')
    >>> lru.set('d', 42)
    >>> [lru.get('a'), lru.get('b'), lru.get('c'), lru.get('d'), lru.get('e')]
    [39, None, 41, 42, None]
    
    >>> lru = LRUCache(3)
    >>> lru.set('a', 39)
    >>> lru.set('b', 40)
    >>> lru.set('c', 41)
    >>> _ = lru.get('a')
    >>> _ = lru.get('c')
    >>> _ = lru.set('b', 666)
    >>> lru.set('d', 42)
    >>> [lru.get('a'), lru.get('b'), lru.get('c'), lru.get('d'), lru.get('e')]
    [None, 666, 41, 42, None]
    
"""
from typing import List, Any, Hashable


class _Node:
    __slots__ = ('_key', '_value', '_prev', '_next')

    def __init__(self, _key: Hashable, _value: Any, _prev: int, _next: int):
        self._key = _key
        self._value = _value
        self._prev = _prev
        self._next = _next


class DoubleLinkedArrayList:
    __slots__ = ('data', 'head', 'tail', 'size', 'capacity')

    def __init__(self, n: int):
        self.data = [_Node(None, None, -1, -1)]*n
        self.head = -1
        self.tail = -1
        self.size = 0
        self.capacity = n

    def is_full(self) -> bool:
        return self.capacity == self.size

    def update(self, index: int, key: Hashable, value: Any):
        self.data[index]._value = value
        self.data[index]._key = key

    def move_front(self, index: int):
        prev = self.data[index]._prev
        nxt = self.data[index]._next
        if -1 <= prev < self.capacity:
            self.data[prev]._next = nxt
        if -1 <= nxt < self.capacity:
            self.data[nxt]._prev = prev

        if index == self.tail:
            self.tail = prev

        self.data[self.head]._prev = index
        self.data[index]._prev = -1
        self.data[index]._next = self.head
        self.head = index

    def push_front(self, key: Hashable, value: Any) -> int:
        self.data[self.size] = _Node(key, value, -1, self.head)
        self.data[self.head]._prev = self.size
        self.head = self.size
        if self.size == 0:
            self.tail = self.size
        self.size += 1
        return self.head

    def get_tail(self) -> int:
        return self.tail

    def get_value(self, index: int) -> Any:
        return self.data[index]._value

    def get_key(self, index: int) -> Hashable:
        return self.data[index]._key


class LRUCache:
    __slots__ = ('data_list', 'key2index')

    def __init__(self, n: int):
        self.data_list = DoubleLinkedArrayList(n)
        self.key2index = {}

    def get(self, key: Hashable) -> Any:
        if key not in self.key2index:
            return None
        index = self.key2index[key]
        self.data_list.move_front(index)
        return self.data_list.get_value(index)

    def set(self, key: Hashable, value: Any):
        if key in self.key2index:
            index = self.key2index[key]
            self.data_list.get_value(index)
            self.data_list.update(index, key, value)
            self.data_list.move_front(index)
            # del old_value
            return
        # else:
        if not self.data_list.is_full():
            index = self.data_list.push_front(key, value)
            self.key2index[key] = index
            return
        # else:
        index = self.data_list.get_tail()
        old_key = self.data_list.get_key(index)
        del self.key2index[old_key]
        self.key2index[key] = index

        old_value = self.data_list.get_value(index)
        self.data_list.update(index, key, value)
        self.data_list.move_front(index)
        # del old_value
        # del old_key


if __name__ == '__main__':
    import doctest
    doctest.testmod()
