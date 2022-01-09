# find_2nd_largest_node(root :Node) -> Node

The biggeest node in a binary tree is the far right node.

So if we search for the second, we assume, that this one ist deleted. So the most far right node is the biggest there.

let us test our these:

We have values of `0` to `7`.

```bitree
balanced: is correct
       4
  2        6
0   1    5   7

list : is correct
0
 1
  2
   3
    4
     5
      6
       7

random: This is more complicated, we will discuss this further
      3
  2       5
 1     4     7
0          6    
```

If we the far right node is a leaf node, the second largest node is its parent.

If the far right node has a left child, than the substrees far right node with the child as root is the second largest node.

## algorithm

1. largest = find the far right in the tree
2. if largest.left:
   1. second_largest = find the far right in the tree with largest.left as root.
3. else
   1. second_largest = largest.parent

### Other cases

1. What will we do, if the size of the tree is not bigger than 2? Let us return Null.
2. If the tree is an Null object? -> Invalid argument Exception or an Assertion Error or somthing  like that

### pseudo code

The second special case does not needed to get checked extra, when we remember the parent and initialize it with Null.

```pseudo
find_2nd_largest_node(root :Node) -> Node
  assert root != Null
  
  parent = Null
  largest = root
  while(largest.right):
    parent = largest
    largest = largest.right

  if largest.left == Null:
    return parent
  else:
    second_largest = largest.left
    while(second_largest.right):
      selcond_largest = second_largest.right
    return second_largest
```

[code](solution.py)
