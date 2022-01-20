# find_longest_palindromic_substring(text :String) -> String

Lets brute force.

```pseudo
find_longest_palindromic_substring(s :String) -> String:
  from, to = _find_longest_palindromic_substring(s, ref to first character in s, ref to last character in s)
  return s[from: to]


_find_longest_palindromic_substring(s :String, from, to) -> pointer, pointer:
    if s[from:to] is palindrom:
        return from, to
    
    ubstring = _find_longest_palindromic_substring(s, from+1, to)
    substrin = _find_longest_palindromic_substring(s, from, to-1)

    return the longer one of ubstring and substrin

```

[code](solution.py)

## some brain farts

Why is it Hard. Maybe there is a better version with time complexity less than `O(N^3)`.
