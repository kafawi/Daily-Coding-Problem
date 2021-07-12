from typing import List


def _lower_pivot_sort(arr: List[int], pivot: int) -> int:
    """ Helper to sort in-place in two buckets determine by a threshold pivot

    Pre: arr is not empty or None

    >>> arr = [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> _lower_pivot_sort(arr,3)
    0
    >>> print(arr)
    [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> arr = [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> _lower_pivot_sort(arr,2)
    1
    >>> print(arr)
    [3, 1, 2, -3, 0, 1, -2, -1]
    >>> arr = [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> _lower_pivot_sort(arr,0)
    4
    >>> print(arr)
    [3, 1, 2, 1, 0, -3, -2, -1]
    >>> arr = [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> _lower_pivot_sort(arr,-2)
    6
    >>> print(arr)
    [-1, 1, 2, 3, 0, 1, -2, -3]
    >>> arr = [-1, 1, 2, -3, 0, 1, -2, 3]
    >>> _lower_pivot_sort(arr,-3)
    8
    >>> print(arr)
    [-1, 1, 2, 3, 0, 1, -2, -3]
    >>> arr = [1]
    >>> _lower_pivot_sort(arr,0)
    1
    >>> print(arr)
    [1]
    >>> arr = [-1]
    >>> _lower_pivot_sort(arr,0)
    0
    >>> print(arr)
    [-1]
    """
    j = len(arr) - 1
    i = 0
    while i < j:
        if arr[i] <= pivot < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            i += 1
        elif arr[i] <= pivot:
            j -= 1
        else:
            i += 1
    # speizalcase if no number below pivot if found -> boundery len(arr)
    return i if arr[i] <= pivot else len(arr)


def find_first_missing_positiv(arr: List[int]) -> int:
    """ Find the first missing positive number.

    >>> find_first_missing_positiv([3, 4, -1, 1])
    2
    >>> find_first_missing_positiv([1, 2, 0])
    3
    >>> find_first_missing_positiv([-1,-3,0,0])
    1
    >>> find_first_missing_positiv([2,3,4,5,5,5])
    1
    >>> find_first_missing_positiv([])
    1
    """
    if not arr:
        return 1
    length = _lower_pivot_sort(arr, 0)
    for e in arr[:length]:
        value = abs(e)
        if value-1 < length and arr[value-1] > 0:
            arr[value-1] *= -1
    for i, e in enumerate(arr[:length]):
        if e > 0:
            return i + 1
    return length + 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
