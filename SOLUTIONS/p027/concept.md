# are_brackets_balanced(bracets_seq :String) $\to$ Bool

We have to validate if a sequence of brackets are well-formed aka balanced.

This means:

- if openening bracket acourse an corresponding closing bracket has to follow.
- inside such an enclosing, other such bracket pairs can be encapsulated.

The corresponding brackets pairs are:

- `(` $\to$ `)`
- `[` $\to$ `]`
- `{` $\to$ `}`

To do this, we can use a stack, thar raises with every opening bracket, and if an corresponding closing bracket is checked, the stack shrinks, but if a non fitting is checked, the whole sequence is not well-formed and the function returns False.

If an closing bracket accourse, but the stack is empty, the sequence is also not well-formed.
And if the stack is in the end not empty, than there is an opening bracket, without its closing partner and the whole sequence is also not well formed. $\to$ The last check is, if the stack is empty.

## tests

### well-formed $\to$ `true`

- `""` empty string
- `"()"`, `"[]"`, `"{}"`
- `"(())"`,`"[[]]"`, `"{{}}"`
- `"([])[]({})"`

### Not well-formd $\to$ `false`

- `"("`, `"["`, `"{"`
- `")"`, `"]"`, `"}"`
- `")("`, `"]["`, `"}{"`
- `"([)]"`
- `"((()"`

## Algorithm

```text
are_brackets_balanced(bracets_seq :String) -> Bool:
  stack :Stack 

  for each bracket in bracket_seq:
    if bracket is opening: 
      stack.push(bracket)
    elif bracket is closing:
      if stack not empty and (stack.peek and bracket are fitting partners):
        stack.pop
      else: 
        return False
    else:
      ignore
  return stack is empty? 
```

[code](solution.py)
[test](test.py)
