"""Test
>>> count_ways_to_climp_up(4, [1,2])
5

>>> count_ways_to_climp_up(1, [2,3,4,5])
0

>>> count_ways_to_climp_up(14, [3,11]) 
2
"""

from typing import Set

def count_ways_to_climp_up(N :int, X: Set[int]) -> int:
  if N < 0: 
    return 0  
  if N== 0: 
    return 1
  count = 0
  for step in X:
    count += count_ways_to_climp_up(N - step, X)
  return count

if __name__=="__main__":
    import doctest
    doctest.testmod()