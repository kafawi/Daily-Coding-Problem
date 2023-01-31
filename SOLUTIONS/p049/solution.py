"""Test

    >>> find_max_subarray_sum([34, -50, 42, 14, -5, 86])
    137
    
    >>> find_max_subarray_sum([-5,-1,-8,-9])
    0
    
"""

from typing import List

def find_max_subarray_sum(numbers :List[int]) -> int:
  max_sum = 0 #init max_sum
  run_sum = 0
  for number in numbers:
    run_sum = max(0, run_sum+number)
    max_sum = max(max_sum, run_sum)
  return max_sum


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    