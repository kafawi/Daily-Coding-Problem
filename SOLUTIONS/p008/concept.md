the question is, how to travers the tree.
use a check method, that checks, if a node is a unival tree.

there for we hat to implement a Node struct.

```
Node<T>:
  value : T
  left  : Node<T>
  right : Node<T>
```

and a check function, and because it is:
```
bool is_unival_tree(root: Node):
  search every node, if he is unival;
```
There are some rules, that we can take advatage of. 
- Every parent of unival tree can be also one, but every parent of a non unival tree is also a non unival tree! 
- every leaf is an unival tree

#### How do we test, that the children are also unival trees?
solution 1: We call the the function recursivly for every node in a breath-first style. -> `O(nlog(n))`. because of the child-parent relationship rule, we always have to travel to the leafs. 
 
solution 2: we start at the bottem (leafs) in a depth first style. There is a good way to do this -> postorder traversal, that ensures, that we move from leaf to root. so we can reuse the results. -> `O(n)`
Let us pseudo code our solution.  

```
is_unival_tree(root: Node) -> bool:
  is_unival = true
  if root.left exists:
    is_unival &= is_unival_tree(root.left)
  if root.right exists:
    is_unival &= is_unival_tree(root.right)
  # space to do stuff
  return is_unival;
```

#### How do we apply the counting? 
Another take is to first go through all nodes and tag them as unival_tree (direct or indirect in a dictionary or somthing like that) and in another traversal, just count the takes,

Or we in one go:
We can have a "global" counting variable or we pass the counting variable every. 
Or we return more than just one value: flag and a counter. I will go with that solution.

```
count_unival_tree(root: Node) -> (int, bool):
  count, is_unival = 0, True
  if root.left exists:
    count_left, is_left_unival = count_unival_tree(root.left) 
    is_unival &= is_left_unival and root has the same value as left
    count += count_left
  if root.right exists:
    count_right, is_right_unival = count_unival_tree(root.right)
    is_unival &= is_right_unival and root has the same value as right
    count += count_right
  
  if is_unival: 
    count += 1
  return count, is_unival
```

We will encapsulate this in a userfrendly version without the bool return value.

[code](solution.py)
