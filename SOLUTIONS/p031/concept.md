# compute_edit_distance(s :String, t :String) -> int

The insertion operation is the operation, so I doubt the easy as difficulty.
So I guessed, that this sounds like a typical problem, that is well known and is teached by many schools. so Why not search for the term?

An I got in a very short time the [Wagner-Fischer algo](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).

Interesting: this is a dynamic programming problem, so we keep a in memory many distances.

## Wagner-Fischer algo

The main idea is, that we look with a composition like:

\[
d_{i-1,j-1} = s_{0:i} \times t_{0:j}, i \in [0, s.length[, j \in [0, t.length[  
\]

or in peudo code:

```text
d :int[-1:s.length][-1:t.length]
d[i,j] = distance of s[0:i] and t[0:j]

```

and the solution is at `d[s.length-1, t.length-1]`

So we can read each record in the matrix `d` as the the edit distance aka. Levenshtein distance of two substrings from `s` and `t`, that always start from the beginning.

some usefull examples:

- `d[n,-1]`: distance of `s[0:m]` and an empty string, which is the eaqual to the length of the substring, because we have to delete `m` characters to get from `s[0:m]` to empty
- `d[-1, n]`: distance of `t[0:n]` and an empty string, which is the equal to the length of the substring, because we have to insert `m` characters to get from an empty string to `t[0:n]`
- `d[0,0]`: distance of the first characters in `t` and `s` : `= 0 if s[0] == t[0] else 1` because substitution is here the only option
- `d[1,1]`: distance of `s[0:2]` and `t[0:2]`:

But how do we calculate the distance at `d[i,j]`?
We look at the previous neighbours, so this is the dynmaic part.
We look for the minimal cost / distance. The path from the neighbour to the current field describe the operation:

```text
VIEW:  s -> t - transform s[i=0:n] into t[j=0:m]
d[i, j] =        : s' =                     : operation
-----------------:--------------------------:------------- 
d[i-1, j  ] + 1  : s[:i] + s[i+1:]          : deletion
d[i,   j-1] + 1  : s[:i+1] + t[j] + s[i:]   : insertion
d[i-1, j-1] + 1  : s[:i+1] + t[j] + s[i+1:] : substitution

if s[i] = t[j]: we can skip, without an operation so:
d[i,j] = d[i-1, j-1], which is somthing like a substitution without replacing
```

For the other way around (`t -> s`), we have to switch deletion and insertion.
Fun fact: deletion + insertion = substitution, but it cost just one distance unit.

For every feld, we need to calculate the indices first, that are by one lower than the current indices. To get the lowest cost, we have to put the minimum of these calculations into the current field.

### pseudo code

The first code will use the whole `s.length+1=M+1`x`t.length+1=N+1` matrix `d`. You can use it to get the operation by, follow the path from the end `d[M,N]` along the lowest values to the beginning `d[-1,-1]`.

We need only the value in `d[M,N]`, so we can optimice the space usage, by remebering only the `j-1` and `j` rows.

```text
compute_edit_distance(s :String, t :String) -> int:
    allocate d :int[-1:s.length, -1:t.length]
    d[-1, -1] = 0

    # s -> empty : deletions
    for i=0, i < s.length, i++:
      d[i, -1] = i+1
    # empty -> t : insertions
    for j=0, j < t.length, j++:
      d[-1, j] = j+1

    for j=0, j < t.length, j++:
        for i=0, i < s.length, i++:
            deletion = d[i-1, j] + 1
            insertion = d[i, j-1] +1
            substitution = d[i-1,j-1] + 0 if s[i] == t[j] else 1
            d[i,j] = min(deletion, insertion, substitution)
 
    return d[s.length-1, t.length-1]
```

### space optimazation

Here we change space Compexity for `O(mn)` to `O(n)`.

Also the distance vectors `d, prev_d` are indexed starting from 0, so we have to shift the indexes.

```text
compute_edit_distance(s :String, t :String) -> int:
    d = [0, 1, 2, 3,..., s.length]
    allocate prev_d :int[0,s.length+1]
    for j=1, j <= t.length, j++:
        swap(prev_d,d)
        d[0] = j
        for i=1, i <= s.length, i++:
            deletion = d[i-1] + 1
            insertion = prev_d[i] +1
            substitution = prev_d[i-1] + (0 if s[i-1] == t[j-1] else 1)
            d[i] = min(deletion, insertion, substitution)
        
    return d[s.length]
```

[code](solution.py)
