
```
check_two_elements_summed_up_to_k: (list:[int], k:int) -> boolean 

true if any two (distinkt) numbers in list adds up to the second argument else false
```

### In one Pass?
with a set, like hashmap or a BST, that stores the all `k-l[i] ` and we test this agains the current position
```
diffs :set(int)
for_each elem in list:
  if is elem in diffs:
    return true
  else:
    diffs.add(k-elem)
return false
```

language: python
[code](solution.py)

run `python solution.py -v` to see tests