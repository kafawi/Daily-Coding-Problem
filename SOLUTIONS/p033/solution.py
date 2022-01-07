"""Tests

    >>> running_median([2, 1, 5, 7, 2, 0, 5])
    2
    1.5
    2
    3.5
    2
    2.0
    2

    >>> consumer = RunningMedianPrinter()
    >>> for num in [2, 1, 5, 7, 2, 0, 5]: consumer(num)
    2
    1.5
    2
    3.5
    2
    2.0
    2
"""

from typing import List
import heapq as hq


class Heap():

    def __init__(self, is_max_heap: bool = False):
        self.is_max_heap = is_max_heap
        self.data = []

    def insert(self, datum):
        if self.is_max_heap:
            hq.heappush(self.data, -datum)
        else:
            hq.heappush(self.data, datum)

    def peek(self):
        if self.size() == 0:
            return None
        datum = self.data[0]
        return -datum if self.is_max_heap else datum

    def pop(self):
        if self.size() == 0:
            return None
        datum = hq.heappop(self.data)
        return -datum if self.is_max_heap else datum

    def size(self):
        return len(self.data)


def running_median(stream: List):
    lo = Heap(True)  # max heap
    hi = Heap(False)
    for num in stream:
        if hi.size() > 0 and num < hi.peek():
            lo.insert(num)
        else:
            hi.insert(num)
        # balancing
        if lo.size() > hi.size() + 1:
            hi.insert(lo.pop())
        elif lo.size() < hi.size():
            lo.insert(hi.pop())

        median = (lo.peek() + hi.peek()) / \
            2 if hi.size() == lo.size() else lo.peek()
        print(median)


class RunningMedianPrinter:
    def __init__(self):
        self.lo = Heap(True)
        self.hi = Heap(False)

    def __call__(self, datum):
        if self.hi.size() > 0 and datum < self.hi.peek():
            self.lo.insert(datum)
        else:
            self.hi.insert(datum)
        # balancing
        if self.lo.size() > self.hi.size() + 1:
            self.hi.insert(self.lo.pop())
        elif self.lo.size() < self.hi.size():
            self.lo.insert(self.hi.pop())

        median = (self.lo.peek() + self.hi.peek()) / 2 \
            if self.hi.size() == self.lo.size() else self.lo.peek()
        print(median)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
