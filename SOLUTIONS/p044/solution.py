"""Test

   >>> count_inversions([])
   0
   
   >>> count_inversions([1])
   0
   
   >>> count_inversions([1, 2])
   0
   
   >>> count_inversions([2, 1])
   1
   
   >>> count_inversions([3, 2, 1])
   3
   
   >>> count_inversions([1, 2, 3])
   0
   
   >>> count_inversions([4, 3, 2, 1])
   6

   >>> count_inversions([2, 4, 1, 3, 5])
   3
   
   >>> count_inversions([5, 4, 3, 2, 1])
   10
"""


def count_inversions(A: list[int]) -> int:
    arr = A.copy()
    count = 0

    def _sort(from_, to):
        length = to-from_
        if length < 2:
            return
        mid = from_ + length // 2
        _sort(from_, mid)
        _sort(mid, to)

        # merge
        nonlocal count
        l, r = 0, 0
        merged = [0] * (length)
        while l < mid-from_ and r < to-mid:
            if arr[l+from_] > arr[r+mid]:
                merged[l+r] = arr[r+mid]
                count += mid-from_-l
                r += 1
            else:
                merged[l+r] = arr[l+from_]
                l += 1

        if l < mid-from_:
            merged[l+r:] = arr[l+from_:mid]
        if r < to-mid:
            merged[l+r:] = arr[r+mid:to]
        arr[from_:to] = merged

    _sort(0, len(arr))
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
