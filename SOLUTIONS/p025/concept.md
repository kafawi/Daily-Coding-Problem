# matches(text :string, pattern :RegexString) -> bool

The definition of our simple regular expression is very small:

- `.` (period) which matches any single character
- `*` (asterisk) which matches zero or more of the preceding element

We have a wildcard and a quantity marker

The special case to consider for later:  super trumpf with `.*`, that matches everything.

## Some ideas, how to solve the problem

because if you think through all "what if"s you will never start. So I will implement it in a simple iterative style, that are validated by a set of tests. In every iteration the test of the previous steps have to return true too, of cause. So we implement in a TDD fashion, that is somewhat like agil, because after every iteration, we will look at the requirments for each step, make eventually additions and design specific test for this kind of requirment, so we grow our understanding of the problem with hopefully all its traps in a smooth and not overwhelming way.

### Iteration 0

Requirments
: every string with no special character will match with the a string with the same order of characters.

test cases
: `input: <text> <pattern> -> output: <return> // note`

```text
 "42"   "42"      -> true // ideom 

 "abc"  "acb"     -> false // wrong order 

 "abc"  "abcd"    -> false // wrong size
 "abc"  "ab"      -> false
 
 ""     ""        -> true   // empty
 "a"    "a"       -> true   // edge to empty
 "a"    "b"       -> false  // edge to empty
```

Not defined / ignored
: `null` as parameter

### Iteration 1

Requirments
: The Wildcard `.` will be matchted correctly.

test cases
: `input: <text> <pattern> -> output: <return> // note`

```text
 ""     "."       -> false  // empty 

 "a"    "."       -> true  // one charater

 "b"    "."       -> true  // one other character 

 "42"   ".2"      -> true   // one wildcard 
 "abc"  "a.c"     -> true   
 "abc"  ".bc"     -> true
 "abc"  "ab."     -> true

 "abc"  "..."     -> true   // match all with correct width
 "efg"  "..."     -> true

 "acb"  "a.c"     -> false  // wrong order 

 "abdc" "a.c"     -> false  // wrong size
 "ac"   "a.c"     -> false  
```

Not defined / ignored
: `.` as any character in an argument for `<text>`

### Iteration 2

Requirments
: The quantifier `*` will work in a combination with all non-special characters.

test cases
: `input: <text> <pattern> -> output: <return> // note`

```text
        <text> <pattern> -> <return> // note 
 ""     "a*"      -> true  // just on character
 "a"    "a*"      -> true   
 "aa"   "a*"      -> true 

 ""     "a*a*"    -> true  // self consuming
 "a"    "a*a*"    -> true   
 "aa"   "a*a*"    -> true
 "aaa"  "a*a*"    -> true    

 "b"    "a*"      -> false // just one character that does not match by one
 "bb"   "a*"      -> false   
 "ab"   "a*"      -> false
 "ba"   "a*"      -> false 

 "a"    "a*aa*"   -> true // the trap 
 
 ITER 1 + ITER 2
 "a"   "a*.a*"    -> true
 ""    "a*.a*"    -> false
 "b"   "a*.a*"    -> true
 "aa"  "a*.a*"    -> true
 "aaa" "a*.a*"    -> true
 "b"   "a*.a*"    -> true
 "aba" "a*.a*"    -> true  
 "ba"   ".a*"     -> true
 "ab"   ".a*"     -> false
 "ba"   "a*."     -> false
 "ab"   "a*."     -> true
```

Not defined / ignored
: `*` as any character in an argument for `<text>`
: `*` as the first character in an argument for `<pattern>`
: `.*`  will be tackled in the next iteration

### Iteration 3

Requirments
: The super trumpf `.*` works correct.

test cases
: `input: <text> <pattern> -> output: <return> // note`

```text
 ""      ".*"      -> true   // just one trumpf
 "a"     ".*"      -> true   
 "ab"    ".*"      -> true

 "abc"   ".*c"     -> true   // tumpf in different places
 "abc"   ".*a"     -> false  
 "abc"   "a.*"     -> true 
 "abc"   "c.*"     -> false 
 "abcd"  "a.*d"    -> true 
 "abcd"  "a.*e"    -> false 
 "abcd"  "b.*d"    -> false

 "a"     ".*a.*"   -> true  // encapsulation
 "ba"    ".*a.*"   -> true
 "abc"   ".*a.*"   -> true 
 "cab"   ".*a.*"   -> true

 "aacac" ".*a.*c"  -> true // the trap
 "aaca"  ".*a.*c"  -> false

 ALL ITERATIONS
 pattern := ".*<tag id=....> ab*c </tag>.*"
 "  <tag id=1234> ac </tag>  42"  pattern -> true
 "  <tag id=1234> ac </taf>  42"  pattern -> false
 "  <tag id=123> ac </tag>  42"   pattern -> false
 "  <tag id=1234> abbbbc </tag>  42"  pattern -> true
```

## Design Ideas

To keep it simple, the evaluation of the inputs - text and pattern - are in a begin to end iteration.

### as a FSM

We can parse the pattern to a finate state machine that will translate for every character in the text as an event and translate to the next state.
With the supertrumpf and the trap like `"...a*aa*..."`, it is necessary to start a sub FSM, to return to this point if the sub FSm failed. (sounds like recursion)

For the case, that a super trumpf `".*"` is presend at the beginning and the end, i will implement the search in a greedy manner. (see Iteration 2)

### FSM as just a pointer / index of the position in text

The FSM is very straight forward because we are handel with strings, that are sequential. So we can use the offset of the current state in the pattern and the offset of the input string.
For every char in a string, we can use the position index to identify the offset.

### upcoming thoughts in iteration 2

in Iteration 2 we need to evaluate each character in the pattern better and independent to the current position of the event /character in text.

The state is determint of the current character and its maybe possible quantifier `"*"`.

If we find a quantifierer, we have to find the possible exit events of this loop state, which is the next different character ind th pattern or the nearest next and same character without a `"*"`.
(We will look at this problem with a twist in the next iteration.)

To handle possible traps, we can jump back with the magic of recurrsion techniques.

#### let's identify the problems in a list

- a state is no more determind going to the next character in the pattern:
  - pattern can be longer or shorter than the to matched text
  - the state counter / pointer in the pattern has to be independent from the char event counter /generator
- despatch the behaviour in two branches of `"*"` and `non "*"`
  - keep functionallity of all `non "*"` like before
  - in a `"*"` state we have to foreshadow to know when to keep the state, going to a False state, or to going to a next state.
    - we have to keep in mind: `"a*a* == a*"`

#### Fist algorithm drawft with focus on keeping the old funtionality

1. for every `char` in `text`:
   1. if `pattern[idx+1]`/state is `*`/optional:
      1. MAGIC
   2. else:
      1. if state.char/`pattern[idx]` is `char` or wildcard `.`:
         1. state = state.next / `idx = +1`
      2. else:
        return False  
2. return when the pattern aka state sequence is somehow finished

So we handle the pattern propagation.
Todo: we have to handle the the bound check by our self. So we have to chek, if the pattern is valid every loop iteration. If not, the text is longer than the pattern and it does not matches.
The state sequence is finished, when we are by one over the last state (in FSM toungh in the termination state). From now I will refer the state with its position/index in the pattern string.

1. for every `char` in `text`:
   1. if `idx` is NOT in `pattern`s bounds: return `False`
   2. if `pattern[idx+1]`/state is `*`/optional:  # here is also a bound check
      1. MAGIC
   3. else:
      1. if `pattern[idx]` is `char` or wildcard `.`:
         1. `idx = +1`
      2. else:
        return False  
2. return idx == pattern.length

#### Tackle the new funtionallity of the quantified state: the MAGIC section

so if we are in a `*` state, we have two options:

1. skip the state and try the next, and if that fails, we check, if the char is fitting this state
2. or try it as long as it fits, and if this terminates in a False state, we move a step back and try the next state, and if that fails 2 step back ...

The fist one is easier to handel, because we can use recurrsion. But for this, we need to call the match funtion with starting indices or just the slices of the strings.

1. skip state and call `matches()` with the `text` starting the current `char` position and a reference to the starting pattern_idx for the next state -> `next_idx = idx + 2`
2. if that terminates with a true state we return `True`
3. else we check if the `char` from the `text` is fitting the current state in the pattern
4. if the `char` does NOT matches the `pattern[idx]` : return False
5. else continue and do not increment the `idx`, because the next char could be also fit this state.

We have to tweek the check, if the state sequence is finished or more in a valid state of beeing terminated, because if all the leftover - or rightover -  states are all optional, we can say, that it is a valid finish.

#### the whole thing

```text
matches(text, text_start, pattern, pattern_start) -> BOOL:
  idx_pattern = pattern_start
  for every idx_text, char in text starting from text_start:
    if idx_pattern is NOT in patterns bounds: return False
    if pattern[idx_pattern + 1] is '*':                      # here is also a bound check
      if matches(text, idx_text, pattern, idx_pattern +2): # skip to next state (recurrsion)
        return True
      else:
        if pattern[idx_pattern] is NOT char or '.': 
          return False
    else:
      if pattern[idx_pattern] is char or '.':
        idx_pattern = +1
      else:
        return False  
3. return idx == pattern.length or all remain states in pattern are optional
```

### iteration 3 aka super trumpf `".*"`

surprisingly nothing to do here

## CODE

[code](solution.py)
[test](test.py)

## Optimazation

This solution is not very maintainable. It does just do the task.

### a real state pattern

A fist Optimasation to give a simple war for adding additional funtionalisation, if we preprocess the pattern string to get a sequence of states that - like a FSM - handle the char by its own.
Also the states can be combined with a strategy pattern like a `quantifyer` and `match_char` behaviore, to keep it. Also the state handels its own transition. Al linked list could be a good fitting data structure.

so the function looks something like this

```text
matches(text, pattern) -> BOOL:
  preprocess pattern into a fsm 
  fsm.handle(text)
  return fsm.is_terminated() and fsm.get_match_status()
```

This will not become a very booklinke state pattern, because we have to keep a stack in track and that will expand the sequence, and in the "context" class is the loop for chars in the text, because the stack is dertemin the position in the text, which character comes next.

With a state pattern, that parses the pattern upfront, we can easy expand with more regex funtionallity.

### optimize zhe pattern to reduce the

Also to reduce the $O(n^2)$ in the optional states, we can preprocess the pattern / states, to keep it more efficiant, like

```text
"a*aa*" -> "aa*a*" -> "aa*"
"b.*a*c" -> "b.*ac" 
```

If you shift pattern states like this, loop over the text in an optional state, till we hit the a escape char from a following state and than make the recurrent call.

## Discussion and Recapitulation

All the optimization possibilities poping instantly into my head and got me stuck and I quited and had to force me, to do the stuff. Overwhelming by overthinking and to many options and details, that are not that important and just destraction to keep it simple.
