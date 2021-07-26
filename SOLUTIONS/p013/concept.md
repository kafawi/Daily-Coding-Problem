# Find the longest Substring in a given String `s` with at most `k` distict characters

`find_longest_substring_with_at_most_k_distict_chars(s: string, k: int) -> string`


A simple go is on every position, test the rest string and count till we got k distinct characters, when it is done, save this one as a candidate and move to the next position. 
This aproach wil take $O(n) = n^2$

```
if k == 0: return ""
if k == 1: return s[0]

longest = ""
charset = Set<char>()
for i=0; i< s.length; i++:
    charset.clear()
    charset.add(s[i])
    for j=i+1; j<s.length; j++:
        if s[j-1] != s[j]:
            continue
        charset.add(s[j])
        # here i have first to check if the indexx j+1 is out of bound
        if charset.size() == k
            substring =s[i:j+1]
            if (longest.length < substring.length):
                longest = substring
            break
return longest
```

### is there a smarter way?
We can formulate a rule: if there is such a substring inside s, then it will start and end with the same character!

There is a smarter way, in the way, that we can search for the next distict character an remeber the position for the next inner loop to start.
but thats will just boost a little and the complexity is still $n^2$.

Another way to do, is to keep track of the last position of every character and slice after the minimum of this positions if we get stumble on a new character. 
This will loop over the input string just one. But it will loop over the character to position map at worst `n` times ($O(n,k) = nk$). But if we assume, that `k < n` or even bettr `k << n` than this is way better than $n^2$.

So we have to store some extra information, but we get a time boost. 

To boost it even further, we can have track of the lowest position in map with a map and a heap combination, but this will go to far for this problem ($O(n,k)=nlogk$).

### Pseudocode
```
find_longest_substring_with_at_most_k_distict_chars(s: string, k: int) -> string:
    char2lastposition<char, int>
    longest = NULL
    substringstart = 0;
    for pos,ch in s:
        if ch is not in char2lastposition:
            if char2lastposition.size == k:
                if longest.length < pos - substringstart:
                    longest = s[substringstart: pos]
                drop_char = get_minimum_char(char2lastposition)  
                substringstart = char2lastposition[drop_char]+1
                char2lastposition.drop(drop_char)
        char2lastposition[ch] = pos
    if longest.length < s.length - substringstart:
        longest = s[substringstart: s.length]
    return longest

get_minimum_char(m: map<char,int>) -> char:
    min_val = Infinit
    min_char = None
    for ch, val in m:
        if min_val > val:
           min_char = ch
           min_val = val
    return min_char
```

in python, to possiblility to return more than 1 value, we can make it a little bit more clearer in the map manipulation.

### edge cases 
if `k` is less than 1: -> return empty string
if `s` is empty: -> return empty string
if `s` is `NULL`: -> return NULL or equivlent  

[code](solution.py)