"""
>>> running_max([10, 5, 2, 7, 8, 7], 3)
[10, 7, 8, 8]

>>> running_max([1, 2, 3, 4, 5], 3)
[3, 4, 5]

>>> running_max([5, 4, 3, 2, 1], 3)
[5, 4, 3]

>>> running_max([1, 2, 3, 4, 5], 5)
[5]

>>> running_max([0, 0, 0, 0, 1], 3)
[0, 0, 1]

>>> running_max([3, 2, 1, 2, 3], 3)
[3, 2, 3]

>>> running_max([1, 2, 3, 2, 1], 3)
[3, 3, 3]

>>> running_max([3, 2, 1, 3, 2], 3)
[3, 3, 3]

>>> running_max([8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2], 2)
[8, 6, 4, 2, 1, 3, 5, 7, 9, 9, 8, 6, 4]

>>> running_max([8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2], 4)
[8, 6, 4, 3, 5, 7, 9, 9, 9, 9, 8]

>>> running_max([8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2], 8)
[8, 7, 9, 9, 9, 9, 9]

>>> running_max([8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2], 14)
[9]
"""

from typing import List
from collections import deque 

def running_max(array :List[int], k :int) -> List[int]:
    assert 0 < k <= len(array)
    assert array and 0 < len(array)
    
    q = deque()
    # 1: init queue
    for i in range(k-1):
        while len(q) > 0 and array[q[-1]] <= array[i]:
            q.pop()
        q.append(i)

    # 2: travers the rest of the array
    maxima = [None]*(len(array) - (k-1))
    for i in range(k-1, len(array)):
        # 1: pop the element, thats not in the k-sized window
        if q[0] <= i-k:
            q.popleft()
      
        # 2: drop all no more maximas candiates 
        while len(q) > 0 and array[q[-1]] <= array[i]:
            q.pop()
    
        # 3: add current element to the back
        q.append(i)

        # 4: print the current running maxima
        maxima[i - (k-1)] = array[q[0]]
    return maxima


if __name__ == "__main__":
    import doctest
    doctest.testmod()