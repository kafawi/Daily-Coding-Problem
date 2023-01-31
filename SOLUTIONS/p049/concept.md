# find_max_subarray_sum(numbers :[int]) -> int

We have to find the maximum sum in the `numbers` that is build by any contiguous subarray.

If we have just negatives, we have a sum of 0 because the empty subarray is also valid.

The time complexity has to be `O(N)`.

## examples

From the task:

```examples
1:
in: [34, -50, 42, 14, -5, 86]
out: 137
because: [34, -50, (42, 14, -5, 86)]

2:
in: [-5, -1, -8, -9]
out: 0
because: for all i is in[i] < 0
```

## brutforce solution

Going throu the array and make for each contiunous subarray a sum, and after that we pick the biggest. (`O(N**2)`)

## keep in mind the negatives

Such a sum is just possible with a subarray that starts at the begining or after an negative value.

Further more, it can only start, after the previous sum is back 0 or lower. (if we assume, that we want to find the largest subarray, that is has to be lower 0.)

## The algorithm

```pseudo
find_max_subarray_sum(numbers :[int]) -> int:
  max_sum = 0 #init max_sum
  run_sum = 0
  for each number in numbers:
    run_sum = run_sum + number   
    if run_sum is negativ:  # start over
       run_sum = 0
    max_sum = max(max_sum, run_sum)
  return max_sum
```

[code](solution.py)
