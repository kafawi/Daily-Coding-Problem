# get_nearest_palindrome(word: String) -> String

We can look at it as a recursive problem.
If the first and the last character match, we can look at the string, without the first and the last character and call the function recursivly.

If they dont match, in two branches:

1. concat the first charater to the end of the string and call the function recursivly without the added character and the first.
2. concat the last character to the beginning of the string and call the function recursivly without the added character and the last.

Then we have to decide, witch variant shorter and lexicographically lower.

The recursion is stopped, when the word of length 0 or 1:

## pseudo code

But we want to create:

```pseudocode
get_nearest_palindrome(word: String) -> String:
  n = word.length
  if n < 2: return word

  first = word[0]
  last = word[n-1]

  palindrom = null
  if first == last: 
    palindrom = first + get_nearest_palindrome(word[1:n-1]) + last
  else:
    pal_first = first + get_nearest_palindrome(word[1:]) + first
    pal_last = last + get_nearest_palindrome(word[:n-1]) + last
    
    # check which is lower
    palindrom = get_min_word(pal_first, pal_last)
  return palindrom

get_min_word(s :String, t :String) -> String:
  min_word = null
  if s.length > t.length:
    min_word = pal_2
  elif s.length < t.length:
    min_word = pal_1
  else: # s.length == t.length
    if s is lexicographically lower t:
      min_word = s
    else:
      min_word = t
  return min_word
```

[code](solution.py)

## extras not needed

Just a reminder, How to check a palindrom in code, but we do not need:

```pseudocode
is_palindrome(word :String) -> Boolean:
  for (i=0, j=word.length-1; i>=j; i++,j--):
    if word[i] != word[j]:
      return False
  return True
```
