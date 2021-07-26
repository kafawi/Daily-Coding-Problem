# this concept is a solution for a nother problem `find_longest_substring_with_at_most_k_same_chars(s: string, k: int) -> string`

`find_longest_substring_with_k_distict_chars(s: string, k: int) -> string`

There are 3 main things to do, while walking through the string:
1. count every distict character
2. track the positions of the distinct characters
3. check if the current character is counted then `k` times. 
   -> we have one substring, (first position an this.) that we have to store in a variable if this is the current longest substring
   -> we drop the count by `1` and drop also the first appearence position


### Pseudocode
```
find_longest_substring_with_k_distict_chars(s, k):
    charmap = Map[char : (number, Queue of the positions)]
    longest_substring = None
    for i=0; i<s.length; i++:
      charmap[s[i]].number++
      charmap[s[i]].queue.enqueue(i)
      if (charmap[s[i]].number == k):
        charmap[s[i]].number--
        start_index = chacharmap[s[i]].dequeue()
        if longest_substring.length < i + 1 - start_index:
          longest_substring = s[start_index : i+1]
    return longest_substring
```




### discussion
What if there is no such substring -> return None

What if k == 0: -> return empty string!  This can be done by making an if statement at the beginning.

If there are more than one such substring of the same length -> retrun any


## Okay this attempt does not return the at most condition. I didnt understnd the problem correctly
`find_longest_substring_with_at_most_k_distict_chars(s :string, k :int): -> string`

A second time think about this:

let us start with the discussion from before:
- if there are no character that appears `k` times -> return `s` : if `k < 1 -> return s` 
- If there are more than one such substring of the same length -> retrun any

How do we use do this this time: simple approach is

go through the whole string. and collect the data, we collected befor, but not evaluate at this time.

```
    charmap = Map[char : (number, positions)]
    longest_substring = s
    for i=0; i<s.length; i++:
      charmap[s[i]].number++
      charmap[s[i]].positions.add(i)
```

Now we have the information to evaluate the area.

1. By ignoring every char, that is less than `k` times countet, we construct a a List of (starting_indxes and end_idexes).

2. if any range include completely another range -> this outer range is droped.

3. now we find the wides range and return the substring.

Let us imaginate it with the example

```
abcda

Collecting stage: before 1
a : 2, [0,4]
b : 2, [1,3]
c : 1, [2]

after step 1:
[(0, 4), (1, 3)]

in step 2:
  0 1 2 3 4
a x       x 
b   x   x

b is in a

after step 2
[(1,3)]

step 3:
max[(1,3) = 2] 

-> return s[1, 3+1] = bcb

```

Step 2 is very time consuming: if we come up with a better solution than `O(n) = n*n`, i will assume


### Pseudocode
```
find_longest_substring_with_at_most_k_distict_chars(s :string, k :int): -> string:
    charmap = Map[char : (number, positions)]
    longest_substring = s
    for i=0; i<s.length; i++:
        charmap[s[i]].number++
        charmap[s[i]].positions.add(i)
    
    candidates : [(start :int, end :int)]

    for each number, positions in charmap:
        if number >= k:
            candidates add all possible pairs of start and end point
    
    valid_candidates = copy(candiates)
    for each a in candidates:
        for each b in candidates:
            if a.start < b.start and a.end > b.end:
                valid_candidates.remove(a)
            if a.start > a.start and a.end < b.end:
                valid_candidates.remove(b)

    if valid_candidate not empty:
        best_candidate = max(valid_candidates, key= x -> x.end - x.start)
        return s[best_candidate.start: best_candidate.end+1]
    else 
      return s
```


#### Optimization
there is a rule.
large substrings can be kicked by smaller substrings. but not vise versa.
so the smalles has the most chance to kick out more candidates.

so if we sort the list of candidates of length, and start at the smallest, that searches the candidates from the longest for inclusion.
Also we can kick out at we go the candidates out of the list. so the next bigger candidate has to deal with lesser comparisons and so on.
If there is no bigger one left, this is the longest substring!

A double linked list would be the best data structure because of the constant complexity by removing an item. 

in pseudocode ->
```
    candidates = sorted(candidates, key= x-> x.end - x.start)

    for each small in candidates:
        for all candidates bigger than small in candidates:
            if the bigger candidate encapsules the small one:
               candidates.remove(bigger candidate)
    
    if candidate not empty:
        best_candidate =candidates.get_biggest;
        return s[best_candidate.start: best_candidate.end+1]
    else 
      return s
```

#### Rework the algorithm - i missunderstood it again

distingt != same

in a new concept file...




[code](solution_of_the_missunderstood.py)
