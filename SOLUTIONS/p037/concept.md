# generate_power_set(set :Set) -> Set[Set]

Idea: The sets in a power set of a subset is also in the power set of its superset.

more formal: `S = elem + S - elem = elem + S'` and `powerset(S) = powerset(S') + { set + elem for each set in powerset(S') }`
So we can use recurrsion.

Another idea is, that we use bit operation, and for each bit, an element in the set is representet. For each bit compilation,
from `000...0` to `111...1`, we can build our subset. This is the well known algorithm. Let us look at both and create both.

## algorithm recurrent

Insert an element into a set twice does not effect the set!

1. if size of set is 0: return powerset with an empty set
2. pop an element and call the funtion with the shorter set
3. for each set from the power set of the shorter set:
   1. add the set to the powerset
   2. add the set included the poped element into the powerset
4. return powerset

```pseudo
generate_power_set_recur(set :Set) -> Set[Set]:
  if set is empty: return a set with an empty set

  elem = get one element of set
  subset = set without elem
  powersubset = generate_power_set_recur(subset)

  for each s in powersubset:
    powerset += s
    powerset += s + elem
  return powerset
```

time = `O(n^2)`

## algorithm bit

1. rearrange the set in an array, so we can access it easy
2. for each combination of n (= size of set) bits:
    1. create set with elements in the array, where corresponding bit is set
    2. put set into the powerset / list

```pseudo
generate_power_set_bitvec(set :Set) -> Set[Set]:
  S = set as array
  
  for bitvec=0; i < 2^S.length; i++:
    subset = empty set
    for j in S.length:
      if j bit is set in bitvec:
        subset += s[j]
    powerset += subset
  return powerset
```

time = `O(n*2^n)`

[code](solution.py)

## Problems

Because pythons set is not hashable and the set in python is a hash set I will return a list that contains the sets.
