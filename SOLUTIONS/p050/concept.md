# eval(term : Bitree_Node) -> int

Given is an already parsed Termin into a binary tree with all leaf nodes as integer values.
All other nodes with children have a one of the arithmetic operation `+`,`-`,`*`,`/`.
The function should return the mathematical correct solution of the term.

To make it like all programminglanguages I know, the devision is strict integer devision: All digits `|x| < 1` will be omitted.

## pre condition

- The `term` is builed correct:
  - Every node with children has exact two childnodes and is an operation. The operationvalues are a enum type.
  - the children have an order to be dertemin with order dependent operaion `-` and `/` left before right -> better other member names in node
  - Every leaf node has an integer value. A negative value is already represented.

## algorithm

This is very easy to make. With the postorder traversal `left -> right -> value`, we can evaluate all nodes.

```pseudo
eval(term):
  if term is integer:
    return term.value

  # else it is an operation
  op1 = eval(term.operant_left)
  op2 = eval(term.operant_right)

  return call corresponding operation in term.value on (op1, op2)
```

## other thoughts, that will not be implemented

We can make a check function to test the term. `is_term_integer(term) -> bool`.
Also we can use this to make it more robust, but such functions live with out user contact in the deeps of a code base. So I will not make invalid tree test cases!

Interesting would be an parser, that create such a term tree.

[code](solution.py)
