# sort_rgb(arr : [`R` or `G` or `B`])

Sort a array with random placed values of `R`,`G` and `B` to a sorted array `R < G < B` in place.

Requirments: in `O(n)` time and in-place. Just swapinbg is allowed.

## My idea

First sort all `R` to the left.
Then sort all `G` in a second run and automaticvally the `B` are in the correct place.

My idea: `O(n) = O(n) + O(n)`

## pseudo code

```pseudo
sort_rgb(arr : [`R` or `G` or `B`]):
  offset = _sort_key(arr, `R`, 0)
  _sort_key(arr, `G`, offset)
    
_sort_key(arr, key, offset):
  i = offset
  j = arr.length -1
  while i < j:
    if arr[i] == key:
       i++
    elif arr[j] != key:
       j--
    else:
       arr.swap(i,j)
  return i
```

[code](solution.py)
