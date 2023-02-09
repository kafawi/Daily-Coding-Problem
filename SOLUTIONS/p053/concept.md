# FIFO with two Stack

Implement a FIFO/queue with two stacks.

```uml
Queue
---------
- :Stack
- :Stack
---------
+ enqueue(element :any)
+ dequeue() :any or -> error
```

## semantic

If the queue is empty, an error is thrown if we try to dequeue.

## How to stack

```uml
Stack
------------
- data :List
------------
+ is_empty() :bool
+ push(element :any)
+ pop() :any or error
```

A Stack is a LIFO (last in first out) data structure.

## From 2 LIFO to 1 FIFO

How do we compose an Queue with two stacks?

Think about a deck of cards: If you put a card on top you are in the enqueue mode.
If you want to draw a card you, you flip the deck upside down to enter dequeue mode and you pick the top one.

So one stack is the dequeue/out one, the other is the enqueue/in one. If we enqueue several times, the in stack get filled. If use now dequeue, we have to pop from the in stack and push it in the out stack, till all cards are "flipped". Than we pop the top element from the out stack and return it. When the next enqueue is called, we have to flip from the out to in, and push the in comming element on top of the in stack.

My solution is not efficient, because you are flip constantly. Worst case is `O(N)` for both operations.

## algorithm

```pseudo
Queue
---------
- in  :Stack
- out :Stack
---------
- flip(from :Stack, to :Stack)
+ enqueue(element :any)
+ dequeue() :any or -> error
---------

flip(from :Stack, to :Stack)
  while from is not empty:
    to.push(from.pop())

enqueue(element :any)
  if out stack is not empty:    # are we in dequeue mode?
    flip(out, in)
  in.push(element)

dequeue() :any or -> error
  if in stack is not empty: 
    flip(in, out)
  if out is empty:
    throw error
  return out.pop()
```

[code](solution.py)
