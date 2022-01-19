# count_inversions(A : [int]) -> int

I admit, I googled it.

So We have to find an Algorithm, that `< O(N^2)`.
A sort algorithm has to solve all inversions. So it is in a sorts heart, so find these inversions.

A good sort algorithms are `O(N log(N)`.

I will choose quick sort and merge sort.

## Quick Sort

```text
[2, 4, 1, 3, 5]    pivot :=first  invariant solving 
                    idx -> val         [indirekt]
[1] 2 [4, 3, 5]       0 -> 2      (2, 1) [(4, 1)]
 1  2 [4, 3, 5]       0 -> 1              
 1  2 [3] 4 [5]       2 -> 4      (4, 3)
 1  2  3  4 [5]       2 -> 3
 1  2  3  4  5        4 -> 5  

                   pivot :=last 
                    idx -> val
[2, 4, 1, 3] 5        4 -> 5
[2, 1] 3 [4] 5        3 -> 3      (4, 3) [(4, 1)]
 1 [2] 3 [4] 5        0 -> 1      (2, 1)
 1  2  3 [4] 5        1 -> 2
 1  2  3  4  5        3 -> 4
```

-> number of invariants `:=` number of `swap`s

## Merge Sort

```text
       [2, 4, 1, 3, 5]                 sequence of element from which half (l,r) 
  [2, 4]             [1, 3, 5]
[2]    [4]         [1]       [3, 5]
 |      |           |      [3]    [5]
 \      /           |       |      |       l0r0
  [2, 4]            |       |      |
      |             |        \    /        l0r0    
      |             |        [3, 5]    
      |             \         /            l0r0r1
      \              [1, 3, 5]              
       \              /                    r0 l0 r1 l1 r2   
        [1, 2, 3, 4, 5]

more detail to inversions relationshipt to l r
(l0,r0) = (2, 1)
(l1,r0) = (4, 1)
(l1,r1) = (4, 3)            
```

When ever a `r[i]` is befor `l[j]`, we have all invariant for the r with all the following elements in `l[k>=j]`.
-> number of invariants `:=` sum of the number of element left in the left array `l`, if an element of the right array `r` is inserted

## Which Algorithm to choose

Because merge sort is guaranteed `O(N logN)`, I will analyse this in more depth.

### check hypothesis with another example

```text
       [5, 4, 3, 2, 1]                 sequence of element from which half (l,r)
[5]    [4]         [3]     [2]    [1]
 \      /           |       |      |       r0l0            1*1 = 1
  [4, 5]            |       |      |
      |             |        \    /        r0l0            1*1 = 1
      |             |        [1, 2]    
      |             \         /            r0r1l0          2*1 = 2
      \              [1, 2, 3]              
       \              /                    r0 r1 r2 l0 l1  3*2 = 6
        [1, 2, 3, 4, 5]                                         10 inversion
```

## Pseudo Code

```pseudo
count_inversions(A : [int]) -> int:
    A' := copy of A {function global scope}
    count := 0  {function global scope}
    _sort(0, A'.length)
    return count

_sort(from, to):
    length = to-from
    if length < 2: return
    mid := floor(length / 2)
    _sort(from, mid)
    _sort(mid, to)
    _merge(from, mid, to) 

_merge(from, mid, to):
    l , r := 0, 0
    merged = empty list
    while (
        l < mid-from = left not empty 
        AND r < to-mid = right not empty
    ):
      if A'[l+from] > A'[r+mid]:
        merged.append(A'[r+mid])
        count :+= length of redual of left = mid-from-l         <- this is the trick
        r++
      else:
        merged.append(A'[l+from])
        l++

    if left not empty:
        merged.concat(left = A'[l+from:mid])   
    if right not empty:
        merged.concat(right = A'[r+mid:to])
    A'[from:to] := merged
```

[code](solution.py)
