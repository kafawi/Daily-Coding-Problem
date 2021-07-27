# List of Problems

with link to solution and a time how log it takes

## The Problems

---

### 1 - Easy

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

[solution](SOLUTIONS/p001/concept.md)

time: 40 min (incl. set up)

---

### 2 - Hard

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

[solution](SOLUTIONS/p002/concept.md)

time: + 2h (solving the problem was fast (15 min), but documentation took long, also got stuck tooooo long with type checking and got distracted a lot. medication wears off at about the beginning of the solving process.)

---

### 3 - Medium

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

[solution](SOLUTIONS/p003/concept.md)

time:

- way too long
- scattered over more days, in chunks of 20 min to 2h
- because not in window of medication
- because of regEx recapture and broken python environment
  - now switch from anaconda to pyCharm

---

### 4 - Hard

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

[solution](SOLUTIONS/p004/concept.md)

time: 3h with research and some a-ha moments

---

### 5 - Medium

This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair.
For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement car and cdr.

[solution](SOLUTIONS/p005/concept.md)

time: 30 min - it was strait forward, after it clicks

---

### 6 - Hard

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields,
it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and
`dereference_pointer` functions that converts between nodes and memory addresses.

[solution](SOLUTIONS/p006/concept.md)

time: 1 day, because cpp.

#### maybe i will revisit this problem with `rust` and its

---

### 7 - Medium

This problem was asked by Facebook.

Given the mapping `a = 1`, `b = 2`, ... `z = 26`, and an encoded message, count the number of ways it can be decoded.

For example, the message `'111'` would give `3`, since it could be decoded as `'aaa'`, `'ka'`, and `'ak'`.

You can assume that the messages are decodable. For example, `'001'` is not allowed.

[solution](SOLUTIONS/p007/concept.md)

time: 30min, 5 min for logic, 25 for documenting, testing implementing and "linting"

---

### 8 - Easy

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```none
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

[solution](SOLUTIONS/p008/concept.md)

time: about 40 min

---

### 9 - Hard

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick 5 and 5.

Follow-up: Can you do this in `O(N)` time and constant space?

[solution](SOLUTIONS/p009/concept.md)

time: day (non continuing) -> because i missunderstood the problem wrong (pre medication kick, i read the problem for, how to get the max sum for non-adjacent numbers and i went bonkerz with an bounded priority queue of 3 and so on...) Check the questions a second time and then prepare with the given testcases, to stop faster if I head to the wrong direction...
after I check the result... -> new take 1 h

---

### 10 - Medium

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

[solution](SOLUTIONS/p010/concept.md)

time: about 2h, because Api unknown in python for me

---

### 11 - Medium

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string `s` and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

[solution](SOLUTIONS/p011/concept.md)

time: more than 2h, because i did not know how to implement a trie, and my attention was wobbleing. The pseudo code is too specific and it could be more general in designing the algorithm.

---

### 12 - Hard

This problem was asked by Amazon.

There exists a staircase with `N` steps, and you can climb up either `1` or `2` steps at a time. Given `N`, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if `N` is `4`, then there are `5` unique ways:

- `1, 1, 1, 1`
- `2, 1, 1`
- `1, 2, 1`
- `1, 1, 2`
- `2, 2`

What if, instead of being able to climb `1` or `2` steps at a time, you could climb any number from a set of positive integers `X`? For example, if `X = {1, 3, 5}`, you could climb `1`, `3`, or `5` steps at a time.

[solution](SOLUTIONS/p012/concept.md)

time: 27 min, This was quite easy, because of a older similar problem. Also the concept truns out to cover more my thought process.  but i am okay with this.

---

### 13 - Hard

This problem was asked by Amazon.

Given an integer `k` and a string `s`, find the length of the longest substring that contains at most `k` distinct characters.

For example, given `s = "abcba"` and `k = 2`, the longest substring with `k` distinct characters is `"bcb"`.

[solution](SOLUTIONS/p013/concept.md)

time: 2,5 h -> i didnt understand the problem correctly, so i missed one particular condition. Medication was taken. Lesson to lern: make sure, you understand the problem right!

The second time, with the right problem to solve, the algorithm was not to complicated, but it takes more than 1h to solve. The missunderstanding is also saved in the folder, if anybody is curious.

---

### 14 - Medium

This problem was asked by Google.

The area of a circle is defined as `πr²`. Estimate `π` to `3` decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is `x² + y² = r²`.

[solution](SOLUTIONS/p014/concept.md)

time: 30 min for the concept, to explain the process, how I would do a Monte Carlo like method. An Eternalty to get a good finishing condition. But it was fun.

---

### 15 - Medium

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

[solution](SOLUTIONS/p015/concept.md)

time: about 1h

---

### 16 - Easy

This problem was asked by Twitter.

You run an e-commerce website and want to record the last `N` order `ids` in a log. Implement a data structure to accomplish this, with the following API:

- `record(order_id)`: adds the `order_id` to the log
- `get_last(i)`: gets the `ith` last element from the log. `i` is guaranteed to be smaller than or equal to `N`.

You should be as efficient with time and space as possible.

[solution](SOLUTIONS/p016/concept.md)

time: about 40 min to learn a bit unittest

---

### 17 - Hard

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:

```non
dir
    subdir1
    subdir2
        file.ext
```

The directory dir contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:

```console
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is `32` (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return `0`.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.

[solution](SOLUTIONS/p017/concept.md)

time: 1h, main solution was fast, but i got bonkers with the extras.

---

### - Hard

This problem was asked by Google.

Given an array of integers and a number `k`, where `1 <= k <=` length of the array, compute the maximum values of each subarray of length `k`.

For example, given `array = [10, 5, 2, 7, 8, 7]` and `k = 3`, we should get: `[10, 7, 8, 8]`, since:

- 10 = max(10, 5, 2)
- 7 = max(5, 2, 7)
- 8 = max(2, 7, 8)
- 8 = max(7, 8, 7)

Do this in `O(n)` time and `O(k)` space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
