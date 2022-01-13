# find_subset_for_sum(numbers :[int], sum :int)-> [int] | null

Without complexity restriction, we can implement the brut force.

## algorithm

### brut force recurrsion

```pseudo
find_subset_for_sum(S :[int], k :int)-> [int]
  if S is empy: return null
  if S[0] == k: return [S[0]]
  subS = find_subset_for_sum(S[1:], k - S[0])
  if subS != null: return subS + S[0]
  # try next
  return find_subset_for_sum(S[1:], k)
```

### a little bit better one

just a little smarter, we can sort the list before and skip all too big ones. So we does not have try each combination

so in this version `S` is sorted:
`S = [12, 1, 61, 5, 9, 2] -> S' = [1, 2, 5, 9, 12, 61]`

```pseudo
find_subset_for_sum(S' :[int], k :int)-> [int]
  if S' is empy: return null
  i = S'.length -1
  while(i > 0 and S'[i] > k): i--
  if S'[i] == k: return S'[i]

  for j in i...0:
    subS = find_subset_for_sum(S[:j], k - S[j])
    if subS != null: return subS + S[0]
  return null
```

### optimazation

To search for the "first" element `S[i]` that is `S[i] <= k`, we could use binary search.

Befor that search, we can check if there are any by check first the minimum of S.

```pseudo
find_subset_for_sum(S' :[int], k :int)-> [int]
  if S' is empy or S'[0] > k: return null
  i = find_rightmost_leq(arr,k)
  if S'[i] == k: return S'[i]

  for j in i...0:
    subS = find_subset_for_sum(S'[:j], k - S[j])
    if subS != null: return subS + S'[0]
  return null

find_rightmost_leq(arr :[int], T :int) -> index:
  # optional short cuts
  if arr[last] <= T : return last
  if arr[first] > T : return -1
  
  l = first = 0
  r = last = arr.length -1
  while(l <= r):
    m = floor of (l+r) / 2
    if arr[m] <= T: l = m + 1
    if arr[m] > T: r = m - 1
  return r
```

To safe the passing overhead. let us just pass an index for the upper bound, because the sorted List is no more manipulated.

[code](solution.py)
