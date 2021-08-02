# Running Max

Print Maxima of all k-sized Subarraies

Based on the running mean i will call this function running max

## The naive algorithm

```pseudo
for start=0,end=k; end <= array.length; start++, end++:
    max = array[start]
    for i=start + 1; i < end; i++ :
        if max < array[i]:
            max = array[i]
    print(max)
```

But this is in time complexity `O(nk)` and not in `O(n)`.
(The space complexity is `O(1)` though.)

## the real problem

The problem has to be solved in `O(n)` time (and `O(k)` space).

## the hint

"You can modify the input array in-place"

## some more cases

```pseudo
k = 3, [5,4,3,2,1] -> 5, 4, 3
k = 3, [1,2,3,4,5] -> 3, 4, 5
k = 5, [1,2,3,4,5] -> 5
k = 3, [0,0,0,0,1] -> 0, 0, 1
```

## Using datastructures like heap

### Heap

A heap has a complexity in space by `O(k)`
To remove a random entry, we hat to balance the heap again. `O(log(k))`.
We have to insert one item `O(log(k))` if balanced.

-> do if we use a heap, we have about a `O(n*log(k))` in time. That is too much.

### Queue

We know, every number after a lesser number will is always the significant one, and the lesser can be dropt.
The other way around we have to remember. the lesser after a big one.

let us use an example for this.

```pseudo
k=3, [9, 5, 2, 7, 8, 7]  to remember 
i=0, [9, 5, 2]           [9, 5, 2]
i=1,    [5, 2, 7]        [7]  because 5 and 2 is lesser than 7
i=2,       [2, 7, 8]     [8] 
i=3,          [7, 8, 6]  [8, 6]
```

We can see, that the maximum is on the leftmost position. If we got this kind of queue, we can make this in about `O(n)`. After the Algorithm is designed, we can see, what the worst case looks like.

A queue can store the indices of the arrays, to keep track of the significant position of the subarray.

We can use a queue where we can pop from both sides.

#### first vage algorithm

1. Build a queue, that got the maximum in the left most place and not contain the lesser previous ones. `O(k)`
2. For every entry in the array starting at position `k`:
   1. drop the oldest (lowest index) entry from the queue, if this is no more in the range of the current range `O(1)`
   2. go through the queue from the back to drop all lower elements that are lesser ore equal than the current element `O(k)`.  Here we have to look for the worst case
   3. add current item into the queue `O(1)`
   4. print left most element in the queue `O(1)`

#### Can we get the 2.2. more clear to get a constant time

To be clear, a item from the input array will only added once and removed once at most. And we travers through the queue just so far till we hit a positien, where the value is greater than the current element.
In theorie this sounds like `O(1)`. But first let us build an algorithm in pseudocode:

```pseudo
running_max(arr :[int], k :int) -> void:
   q : Dequeue = new Dequeue(size=k) 
   # 1: init q with the first k-1 elements
   for i = 0; i < k-1; i++:
      # 1: drop all no more maxima canidates 
      while q has elements and arr[q.peek_back()] <= arr[i]:
         q.pop_back()
      # 2: add current element to the back
      q.push_back(i)

   # 2: travers the rest of the array
   for i = k-1; i < arr.length; i++:
      # 1: pop the element, thats not in the k-sized window
      if q.peek_front() <= i-k:
         q.pop_front()
      
      # 2: drop all no more maximas candiates 
      while q has elements and arr[q.peek_back()] <= arr[i]:
         q.pop_back()
      
      # 3: add current element to the back
      q.push_back(i)

      # 4: print the current running maxima
      print(arr[q.peek_front()])
```

For the sake of dylexia and so few variables I called the `max_filter_queue` just `q`. Possible other names are `max_indices_filter_queue` or `max_funnel`.
To minimize duplcation of code I initialize the queue with just the first `k-1` elements, because the first max is valid at the `k-1` position.

Lets look at some cases to count the operations (not the conditions):
Because we are sure to add an element, we just focus on the loops and conditins in 1 and 2.1 and 2.2.
We can compare the numbers, if we add to the total the length o the queue at the end, because `k` should be the max diffence from the best to the worst to the best cases.

```pseudo
input and queue     :       steps
k=3 [1, 2, 3, 4, 5] : 1.1 2.1 2.2 total
    [1]               0            0        
    [x  2]            1            1
    [   x  3]             0   1    1
       [   x  4]          0   1    1
          [   x  5]       0   1    1
                                   4 + 1

k=3 [5, 4, 3, 2, 1] : 1.1 2.1 2.2 total
    [5]               0            0
    [5, 4]            0            0
    [5, 4, 3]             0   0    0
     x [4, 3, 2]          1   0    1
        x [3, 2, 1]       1   0    1
                                   2 + 3

k=3 [3, 2, 1, 2, 3] : 1.1 2.1 2.2 total
    [3]               0            0
    [3, 2]            0            0
    [3, 2, 1]             0   0    0
     x [x  x  2]          1   2    3
          [   x  3]       0   1    1
                                   4 + 1
k=3 [1, 2, 3, 2, 1] : 1.1 2.1 2.2 total
    [1]               0            0
    [x  2]            1            1
    [   x  3]             0   1    1
       [   3, 2]          0   0    0
          [3, 2, 1]       0   0    0
                                   2 + 3

k=3 [3, 2, 1, 3, 2] : 1.1 2.1 2.2 total
    [3]               0            0
    [3, 2]            0            0
    [3, 2, 1]             0   0    0
     x [x  x  3]          1   2    3
          [   3, 2]       0   0    0
                                   3 + 2
```

Interestinly: this seems total stable `O(n)`. Let us see, if `k` has an effect:

```pseudo
input and queue                                :       steps
k=2 [8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2] : 1.1 2.1 2.2 total
    [8]                                          0            0
    [8, 6]                                           0   0    0
     x [6, 4]                                        1   0    1
        x [4, 2]                                     1   0    1
           x [2, 0]                                  1   0    1
              x [x  1]                               1   1    2
                   [x  3]                            0   1    1
                      [x  5]                         0   1    1
                         [x  7]                      0   1    1
                            [x  9]                   0   1    1
                               [9, 8]                0   0    0
                                x [8, 6]             1   0    1
                                   x [6, 4]          1   0    1
                                      x [4, 2]       1   0    1
                                                             12 + 2

k=4 [8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2] : 1.1 2.1 2.2 total
    [8]                                          0            0
    [8, 6]                                       0            0
    [8, 6, 4]                                    0            0
    [8, 6, 4, 2]                                     0   0    0
     x [6, 4, 2, 0]                                  1   0    1
        x [4, 2, x  1]                               1   1    2
           x [x     x  3]                            1   2    3
                [      x  5]                         0   1    1
                   [      x  7]                      0   1    1
                      [      x  9]                   0   1    1
                         [      9, 8]                0   0    0
                            [   9, 8, 6]             0   0    0
                               [9, 8, 6, 4]          0   0    0
                                x [8, 6, 4, 2]       1   0    1
                                                             10 + 4

k=8 [8, 6, 4, 2, 0, 1, 3, 5, 7, 9, 8, 6, 4, 2] : 1.1 2.1 2.2 total
    [8]                                          0            0
    [8, 6]                                       0            0
    [8, 6, 4]                                    0            0 
    [8, 6, 4, 2]                                 0            0
    [8, 6, 4, 2, 0]                              0            0
    [8, 6, 4, 2, x  1]                           1            1
    [8, 6, 4, x     x  3]                        2            2
    [8, 6, x           x  5]                         0   2    2
     x [x                 x  7]                      1   2    3
          [                  x  9]                   0   1    1
             [                  9, 8]                0   0    0
                [               9, 8, 6]             0   0    0
                   [            9, 8, 6, 4]          0   0    0
                      [         9, 8, 6, 4, 2]       0   0    0
                                                              9 + 5
```

This is pritty solid. So let us implement this.

Instead of printing I will return a list of the maxima.

[code](solution.py)

### Extra because I want to: Double Ended Bounded Queue

This pseudocode ignores the allocation and deallocation, so it is suited for base types like int best.

Also I want to make use of negative indexing for easy retrieve by counting from the other side.

```pseudo
class DEQueue<T>:
   data :[T]
   LEN :int
   first :int
   size :int

   DEQueue(len: int):
      LEN = len
      data = int[LEN] 
      first = 0
      size = 0

   is_empty() -> bool:
      return 0 == size
   
   pop_front() -> T:
      if is_empty():
         CRASH
      val: T = data[first]
      first = (first + 1) % LEN
      size--
      return val
   
   pop_back() -> T:
      if is_empty():
         CRASH
      last = (first + size) % LEN
      val :T = data[last]
      size--
      return val
   
   peek(pos :int) -> T:
      if is_empty() or not size <= pos < size:
         CRASH
      i =  pos % (size +1)
      return data[(first+i) % LEN]
   
   push_front(val: T, offset = 0: int) -> void:
      if size >= LEN or not -(size+1) <= offset <= size:
         INVALID CRASH
      offset = offset % (size +1)
      i : int = (first - 1 + offset) % LEN
      data[i] = T
      first = i
      size = size + 1 - offset

   push_back(val: T, offset = 0: int) -> void:
      if size >= LEN or not -(size+1) <= offset <= size:
         INVALID CRASH
      offset = offset % (size() +1)
      i :int = (first + size - offset) % LEN
      data[i] = T
      size = size + 1 - offset
```
