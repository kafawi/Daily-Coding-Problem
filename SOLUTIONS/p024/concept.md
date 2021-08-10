# Lockable Binary Tree

first let us make some pictures to get a better understanding.

- `n` is node id
- `n:O` is an unlocked node
- `n:X` is an locked node

```pseudo
            0:O
    1:O             2:O
3:0     4:O     5:O     6:0
```

## The rule to lock

You can lock and unlock if:

- all descendants are unlocked  
- all ancestors are unlocked

## the class diagramm

```pseudo
class Node<T>:
  - value_ :T
  - parent_ :Node 
  - left_ :Node 
  - right_ :Node

  + is_locked() :bool
  + lock() :bool 
    -> true if successful, else false
  + unlock() :bool
    -> true if successful, else false
  
  + get() -> T
  + set(value :T)
```

## let us make some lock trys on the tree above

- `n` is node id
- `n:O` is an unlocked node
- `n:X` is an locked node
- `n:o` o `n:x` to indicate the involved nodes

```pseudo
            0:O
    1:O             2:O
3:0     4:O     5:O     6:0

1.lock() -> true
            0:o
    1:X             2:O
3:o     4:o     5:O     6:0

0.lock() -> false
            0:O
    1:x             2:o
3:0     4:O     5:o     6:o

5.lock() -> true
            0:o
    1:X             2:o
3:0     4:O     5:X     6:0

1.unlock() -> true
            0:o
    1:O             2:O
3:o     4:o     5:X     6:0
```

## algorithm

The algorithm is for both `lock` and `unlock` pretty the same.
The order of traversal is not really nessessary.

1. up, to check if any node is `locked`
2. down, for each child, check if ny node is `locked`

But this approache is more $O(n)$ and not $O(h)$.

the first climbing `up` is everytime $O(h)$.

but the climbing `down` is $O(2^h) = O(2^{log2(n)})= O(n)$

## can we skip the down climbing by an extra flag

We can skip the down climbing, if we mark all ancestors of a locked nodes with a `locked_branch_` flag.
So if we try to lock an node, we can check its `locked_branch_` flag instead of climbing down the tree under that node.

If we want to unlock a node, we can check it like above, but we have also unset the flags by climbing up again and check for every visited node if the other child is in a `locked_branch_`.

## lets do the example from above with this aproache

node format: $id:l:b$
$id \in \natnums, l,b \in \{x,X,o,O\} $

- `id` : id of node
- `l` : indicates, if it is locked (`X : is locked`, `O : is not locked`)
- `b` : locked branch flag  (`X :  is in a locked branched`, `O : is not locked`)
- if `l` or `b` is lower case, `x,o`, than this fields are toucht by the method call.

```pseudo
            0:O:O
    1:O:O           2:O:O
3:O:O   4:O:O   5:O:O   6:O:O

1.lock() -> true
            0:o:x
    1:x:O           2:O:O
3:O:O   4:O:O   5:O:O   6:O:O

0.lock() -> false
            0:O:x
    1:X:O           2:O:O
3:O:O   4:O:O   5:O:O   6:O:O

5.lock() -> true
            0:O:x
    1:X:O           2:o:x
3:O:O   4:O:O   5:x:O   6:O:O

1.unlock() -> true
            0:O:x
    1:o:O           2:O:X
3:O:O   4:O:O   5:X:O   6:O:O
```

## algorithm v2

I choose the loop over the recurrsion, because of the less overhead.

### is node lockable / unlockable

1. if this nodes is in a locked branch (has min one decendend that is locked):
   1. return False
2. tmp = this node parent
3. while tmp is not null:
   1. if tmp is locked:
      1. return False
   2. tmp = tmps ancestor
4. return True

### lock

1. if this node is already locked:
   1. do nothing and return True
2. if this node is not lockable:   // is in a locked branch or has a locked ancestor
   1. do nothing and return False
3. else tmp = this nodes parent
4. while tmp is not null and tmp is not in a locked branch:
   1. tag tmp with a locked branch flag
   2. tmp = tmps ancestor
5. set this nodes locked flag
6. return True

### unlock

1. if this node is already unlocked:
   1. do nothing and return True
2. if this node is not lockable: // is in a locked branch or has a locked ancestor
   1. do nothing and return False
3. else tmp = this node
4. while tmp has an ancestor and tmps sibling is not in a locked branch:
   1. unset tmps ancestors locked branch flag
   2. tmp = tmps ancestor
5. unset this nodes locked flag
6. return True

### class diagramm v2

```pseudo
class Node<T>:
  - value_ :T

  - is_locked_ :bool
  - is_locked_branch_ :bool

  - parent_ :Node 
  - left_ :Node 
  - right_ :Node

  + is_locked() :bool
  + lock() :bool 
    -> true if successful, else false
  + unlock() :bool
    -> true if successful, else false
  
  + get() -> T
  + set(value :T)
```

### other

`set` will be secured by the lock flag just to show that a lock has a meaning...

lets lock'n'roll

[code](solution.py)

### afterthoughts

the `in_locked_branch` flag is a bit too vage. A better is a name like `is_any_descendent_locked`.

I will refactor this in the solution.

In my solution, will always return true, if the node is locked, because the conditions for a locked node is everytime a condition, where a locked node can be unlocked.
This is because an already unlocked node will return always True, because nothing is to do.

If we remove this conviniant condition, we will have cases, where we try to unlock an already unlocked node and we will encounter, that maybe an descendent or an ancestor is locked, so we will return False in this case. But I think, that is not very smart, because, why should you unlock an already unlocked node?
