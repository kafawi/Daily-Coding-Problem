# List of Problems 
with link to solution and a time how log it takes 

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