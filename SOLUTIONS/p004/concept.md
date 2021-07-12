The easiest way would be to sort the array and then walk through, till we find the first gap in when it is in the area of positive numbers.
```
get_first_missing_positiv(arr: [int]) -> int:
  sort(arr)
  min = 1
  for i=0; i < arr.length-1; i++:
    if arr[i] <= 0 : continue
    if arr[i+1] - arr[i] > 1: return arr[i] + 1
  return arr[arr.length-1] + 1 
```

But this is not in linear time, because sorting is `O(n) = n log(n)`.

Another approach would do it in linear time but not in constant memory, 
- when we go through the array and memorize all positive ones in an array of the size of the biggest integer at the index of the entrie value
  - (that is constant but too big, but we want to avoid collision)
- then walk through this new array from the max and the min of our input, till we find the gap

This will run in `O(n) = n` 
But it will take a lot of memory, it is constant, but not practical because `n` is mostly lower than the biggest integer value `c`
- :`O(n) = c >> n`

### Other approaches
We could use heaps, but this violates the constant memory constrain.

I have to research...

After I found something on [StackOverflow](https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti).
Credits goes to pmcarpan.

I will try top explain it, so it does more sense:
Assume we have an array of just positiv entries: `e > 0`
If we use the entries as indexes, we can tag the position to indicate, that this position is as value in the array. 
- to tag the position and keep a possibility to get the value, we set the sign to negative 
At a second go, we can traverse the array and find the first positive (not tagged) index. This first index is the missing first value.

- the duplicates will remain as negative (not toggling)
- the value is retrieved with the absolute operation.
- If all are negative, the first missing is the highest index + 1

If we assume, that the arrays indexes starts at 1, this algorithm is more readable:

```
find_first_missing_positiv(arr: [int]) -> int:
  length = lower_pivot_sort(arr, 0) // all lower and  pivot are at a highter indices and all greater are : see below for implementation
  for i = 1; i <= length; i++:
    value = abs(arr[i])
    if value < length:
      if arr[value] = negativize(arr(value))  // arr[value] *= -1 if arr[value] < 0 else 1
  
  for i = 1; i <= length; i++:
    if arr[i] > 0:
      return i
  
  return length+1
```

Here the array starts with index `0` to `length - 1` 
```
lower_pivot_sort(arr: [int], pivot: int) -> int:
  j = arr.length-1
  i = 0
  while i < j:
    if arr[i] <= pivot and arr[j] > pivot:
        swap(arr, i, j)
        j--
        i++
    else arr[i] <= pivot:
       j--
    else:
       i++
    
    return maybe i // boundery -> length of the outsorted array of e > pivot
```

[code](solution.py)

afterthoughts, 
It is the combination of my first 2 thoughts...




