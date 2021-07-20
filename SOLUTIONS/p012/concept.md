This Problem is simelar to the one, where we have to get count the possible encodings.
So there for, my algorithm is like this. for the simpicity, we take first just `1` or `2` stairs at a time.

```
count_ways_to_climp_up(num_stairs :int) -> int:
  if num_stairs < 0: return 0  
  if num_stairs == 0: return 1
  count = 0
  count += count_ways_to_climp_up(num_stairs -1)
  count += count_ways_to_climp_up(num_stairs -2)
  return count
```

For the version with step width set, we have to pack the reurrent calls in a loop:
```
count_ways_to_climp_up(num_stairs :int, steps: Set[int]) -> int:
  if num_stairs < 0: return 0    // not a possible way to climp
  if num_stairs == 0: return 1   // found one possible way
  count = 0
  for each step in steps:
    count += count_ways_to_climp_up(num_stairs -1, steps)
  return count
```

#### Some edge cases:
What if we have a staicase with "num_stairs <= 0"  at the beginning? 
For simplicity, we can wrap the recurrent function in a public wrapper, that handels this type of cases with an Exception. But that is not nessecary for this prototype. 

Also if the set is empty, this function will stuck, so this can  also be avoid by check the set in the wrapper / decorator.


I will convert `num_stais -> N` and the set `steps -> X` to take the given variable names.
[code](solution.py)