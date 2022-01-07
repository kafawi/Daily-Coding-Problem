# running_median(stream :[number]) -> std.out numbers

To calculate the median, we need to remember, what numbers accure before.

So we have to store all numbers that is at least `O(n)`.

Also this algorithm should run in an minimum of time.

The fastes way to insert a number into a list, depends on the type of list.

For an array we can use quick search `O(log n)` the position in a sorted array, but in the worst case we have `O(n)` to insert it.

For a linked list, we search in `O(n)` and insert it in `O(1)`.

But `n` is changing and we have to be faster in a stream.

## Why not heaps

We can use heaps to find the median to, by deviding the stream in a lower side and greater side.

The lower side is a max heap and the bigger side is a min heap.

For every insert, we can work like this.

```code
lo : max_heap
hi : min_heap
for num in numbers:
    if hi.size() > 0 and num < hi.peek():
        lo.insert(num)
    else:
        hi.insert(num)
    # balancing
    if lo.size() > hi.size() + 1:
        hi.insert(lo.pop())
    elif lo.size() < hi.size():
        lo.insert(hi.pop())

    if hi.size() == lo.size():
        median = (lo.peek() + hi.peek())/2
    else: 
        median = lo.peek()
    print(median)
```

So if we ignore the reallocation of a bigger space for the heaps, we have a overall time complexity of `O(log n)`. That is the best, what we can do.

Because we have to do it for a stream, we can make an Consumer object, that holds the heaps but reacts just to one item at a time.

[code](solution.py)
