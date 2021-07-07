"""
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

>>> check_two_elements_summed_up_to_k([10, 15, 3, 7], 17)
True

More Tests:
  >>> check_two_elements_summed_up_to_k([], 17)
  False

  >>> check_two_elements_summed_up_to_k([17], 17)
  False

  >>> check_two_elements_summed_up_to_k([0,0], 0)
  True

  >>> check_two_elements_summed_up_to_k([7, 16, -1, -5, 12], 11)
  True

  >>> check_two_elements_summed_up_to_k([7, 16, -1, -5, 12], 1000)
  False

  >>> check_two_elements_summed_up_to_k([1, 2, 3, 4], 6)
  True
"""


def check_two_elements_summed_up_to_k (l:list[int], k:int) -> bool:
  """Returns True if two elemens in the list l adds up to k, else False"""
  diffs = set()
  for elem in l:
    if elem in diffs:
      return True
    else:
      diffs.add(k-elem)
  return False



if __name__=='__main__':
  import doctest
  doctest.testmod()