# Stack[Comparable type]

A Stack is a simple linked list, that grows in one direction by appanding one element with the `push` command, and shrinks at the same ending by its `pop`. With the possibility of a `max` function, that returns the current maximum in the stack list, this datastructure needs an additional list that pushes the index of the value, that is added by `stack.push(value)` to this maximum list, if the previous maximum is less than this `value`.
If a value is popped, We have to compare the index of the stacks top aka the popped value with the value in the maximum list last. If they match, we pop this list also.

To make all operation in `O(1)`, we have to think as the indexes as reference to the list node.

## algorithm

I will go with the error, if someone try to `pop` or `max` an empty stack.

```pseudo

struct Node[T]:
  - val :T
  - prev :Node[T]

class Stack[T]:
  - top : Node[T] := NULL
  - max_top : Node[&Node[T]] := NULL

  + push(val :T):
      # append a new node on the val list
      top = Node(val := T, prev := top)
      if max_top is NULL or max_top.val.val < val:
        # append a this new node to the max list
        max_top := Node(val := top, prev := top_max)
  
  + pop() -> T:
    if top is empty aka. is NULL:
      -> ERROR
    if top is max_top.val:
      # pop max list
      max_node := max_top
      max_top := max_node.prev
      delete max_node
    node := top
    # pop val list
    top := top.prev
    val := node.val
    delete node
    return val

  + max() -> T:
    if max_top is empty aka. is NULL:
      -> ERROR
    return max_top.val 
```

[code](solution.py)
