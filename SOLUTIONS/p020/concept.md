# Find Merging Node

## Why merge

The word merge discribes it better for me. An intersection is more a one time thing and after that the list are on their own again.
The lists starts on their own, but on this special node, they merge.
Maybe I worked too long with **git**, where commits are sort of organized as a non circular graph and when you merge two branches (look like two linked list) and one commit is the intersection node.

## Constrains

Do this in `O(M + N)` time (where `M` and `N` are the lengths of the lists) and constant space.

## How to

We know of the nature of a single linked list, that every node defines its own single linked lists.
And at the intersection / merge node, this sublist is the very same for the rest nodes.
So we know, that the two list have the same tails, we have to run through the longer list till we get a sublist of the same length of the smaller one.
At this point the only thing to do, is to compare the nodes for every node we visit.

So the algorithm is like this.

1. for List A get the length N
2. for List B get the length M
3. sort the Lists and length to longer and shorter
4. get the node in the longer list at position `longerlen - shorterlen`
5. traverse the shorter list and the sublist of the longer one till both have the same node.

## in pseudocode

We make it more general, by retrieve the lengths by traversing. Otherwise we have a time complexity of `O(max(M,N))`. So it is more work.

```pseudo
find_merging_node(A: List, B: List) -> Node:
    N = retrieve_length(A)  # N 
    M = retrieve_length(B)  # M

    shorter :Node = A.first if N < M else B.first
    longer :Node = B.first if N < M else A.first

    # running to get longer to the same length of shorter
    for |N - M| times:
       longer = longer.next
    
    while shorter and longer is not shorter:
        longer = longer.next
        shorter = shorter.next
    
    return shorter
```

```pseudo
retrieve_length(list :List) -> int:
    tmp :Node = list.first
    length :int = 0
    while tmp:
        length++
        tmp = tmp.next
    return length 
```

## Is `|N - M|` the correct offset?

by example:
$ N=2, M=3 : |N - M| = 1$ correct
$ N=3, M=0 : |N - M| = 3$ correct

## Test cases

The intersection node is...

1. somewhere in the middle
   1. with same length like in the example
   2. with different length
2. the first node of both
3. the very last node
4. nowhere
   1. one list is empty
   2. both list are filled but no intersection

[code](solution.py)
