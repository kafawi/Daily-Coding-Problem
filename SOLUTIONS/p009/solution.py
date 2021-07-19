"""Test
>>> calc_largest_non_adjacent_sum([2, 4, 6, 2, 5])
13

>>> calc_largest_non_adjacent_sum([5,1,1,5])
10

Special test cases for the different definition, what a sum is!

>>> calc_largest_non_adjacent_sum2([-2, -1, -3, -5])
-1

>>> calc_largest_non_adjacent_sum3([-2, -1, -3, -5])
-5
"""

from typing import List, Tuple

def calc_largest_non_adjacent_sum(numbers :List[int]) -> int:
    prev_sum :int = 0
    max_sum :int = 0
    for number in numbers:
        new_max_sum :int = max(prev_sum + number, max_sum)
        prev_sum =  max_sum
        max_sum = new_max_sum
    return max_sum

def calc_largest_non_adjacent_sum2(numbers: List[int]) -> int:
    max_sum = calc_largest_non_adjacent_sum(numbers)
    if max_sum == 0:
        max_sum = max(numbers)
    return max_sum


def calc_largest_non_adjacent_sum3(numbers: List[int]) -> int:
    class PrioQueue:
        idxnums_ = [None, None, None]

        def add(self, idxnum :Tuple[int, int]):
            cmp = lambda a, b: a[1] - b[1]
            for i in range(3):
                if self.idxnums_[i] is None or cmp(self.idxnums_[i], idxnum) < 0:
                    self.idxnums_ = self.idxnums_[:i] + [idxnum] + self.idxnums_[i:2]
                    break
 
        def pop_all(self) -> List[Tuple[int, int]]:
            return self.idxnums_

    max_sum = calc_largest_non_adjacent_sum(numbers)
    if max_sum == 0:
        maxima= PrioQueue()
        for idxnum in enumerate(numbers):
            maxima.add(idxnum)
        # get a simple list
        maxima = maxima.pop_all()

        # lambdas for more readable code
        is_adjacent = lambda a, b : abs(a[0] - b[0]) == 1
        add_idxnum = lambda a, b : a[1] + b[1]
        max_sums = list()
        if not is_adjacent((maxima[0]), (maxima[1])):
            max_sums.append(add_idxnum((maxima[0]),(maxima[1])))
        if not is_adjacent(maxima[0], maxima[2]):
            max_sums.append(add_idxnum((maxima[0]),(maxima[2])))
        if not is_adjacent(maxima[1], maxima[2]):
            max_sums.append(add_idxnum((maxima[1]),(maxima[2])))
        max_sum = max(max_sums)

    return max_sum


if __name__=="__main__":
    import doctest
    doctest.testmod()
