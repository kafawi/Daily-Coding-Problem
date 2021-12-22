# remove_from_back(list :SLL, k :int) -> element

From a single linked list the `k`th element from the back has to be removed.

## The simplest way

1. get the length `l` of the list (one pass to count)
2. remove the `l - k` element (oe pass to step to `l - k`th element from the front)

Thats are tow passes in total. But thats agains the contrains of the problem:
Do this in constant space and in one pass.

## My solution

`k` is also the distance from the tail of the list to this element. So mind the gap. Also just keep in mind that we need actually the element befor `k`th from the back by making an extra step.

1. count = 0
2. walker = list.head
3. while (count != k+1):  
   1. walker = walker.next
   2. count += 1
4. predecessor = list.head
5. while (walker is not the end / tail):
   1. walker = walker.next
   2. predecessor = predicessor.next
6. to_remove = predecessor.next
7. predecessor.next = to_remove.next
8. to_remove.next = Nothing
9. return to_remove

## thoughts on this

I dont know, if this is cheating, because we technically do a double pass in the second half.

At step 3, a for loop is a better way to do `for(i=0; i<k; walker = walker.next)`
also we have to get the predecessor of k, so we have to walk one step further.
`for(i=0; i<k+1; walker = walker.next)`. If the walker is the end of the List, the element to remove has no predecessor and we have to manipulate the head variable of the list, because the value of this variable is the element to remove.

To make it a little easier for me, I will make a helper funtion `_get_from_back(list, k)` to retrieve the `predecessor` node with calling it with `k+1`. Remove is just the extra constant steps to bend the next pointers.

[code](solution.py)
