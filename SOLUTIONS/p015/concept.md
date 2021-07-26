# picking random element out of stream uniformly

This is very hard, because if we do not know how long this stream is, we cannot say, when that this is randomly.

If we know, how long, this is very easy, because, we can use a random number generator to determin, when to make the pick.

if we do not know, you have to guess. A good guess would be, to make chunks of the stream and store a random element. After the stream is finished, you pick up a random ou of the choosen.
If the last chunk is smaller than the others, we have to take that in mind, to calculate the correct propability of all chunks wright. That is: $\frac{chunksize}{number of elements}$

If we run out of space when the stream is no finished, we have to prepick the first chunks and comprimise the list.

I have to draw these trees of possibillity produts to check my solution.

With this solution, it is a divide and conquer method.

Another problem is, if the stream is never finish, how do we pick?

## An example

We have a total stream of exactly 3 chunks to make it simple. Let chuck size be `nc` -> `nc*3 = n` number of elements. to total Propability for a unifom pick is for every element `p = 1/n = 1/(3*nc)`

After the first chunk we have choosen one element with the properbility `p'_0 = 1/nc`.

This one is the only one `p_0 = 1/nc`.

After the second chunk we have choosen another element out of the second chunk with `p'_1 = 1/nc`.

To keep one of them, we have to pick one with the same propability -> `p_01 = 1/nc * 1/2`

After the third chunk we have choosen one element out of the third chunk with `p'_3 = 1/nc`.

To keep one of them, we have to weight carefully, because the choosen one of the first two chunks has 2 times more the chance to get picked. `p_01 = 1/nc * 1/2 * 2/3` and `p_3 = 1/nc * 1/3`.

So the question is, where is the threashold or what is the propability, to change the previous decision. That is `p_new = 1/nc * 1/chunk_number`

We can see, that `p_01 = 1/(3nc) = 1/n = p_3`.

So this is also true if we choose a chunk size of 1 and that is for every stream size siutable.

`p_new = 1/number_of_streamed_elements -> p_old = 1-p_new`

### The algorithm

```pseudo
choosen_one :E
element_cnt = 0
    for e in stream:
        element_cnt += 1
        p = random(from=0,to=1)
        if p < 1/element_cnt:
            choosen_one = e
return choosen_one
```

A typical streamfunction does somthing with one element at a time, sometimes its neighbours.
To change this whole algorithm and cristalize the core funtion into a funktion, we need something like a global or static variabel to store the `choosen_one` and the `element_cnt`.
In Python we can create a callable Class.

### How do we test this?

For the simplicity I go with a List as stream. And make a Test by running this several times and test if this is about uniform distributed.

[code](solution.py)
