# build_tree(preorder :[T], inorder :[T]) -> Tree[T]

The task is, to build a binary tree from the presentaion list of the pre- and the inorder.

We know the root of an tree is represented as the first entry in a preorder list. And in the inorder list, this node devide the list into the left subtree, and the right subtree. By building the tree in preorder, and determin which nodes are in the left and right subtree with the inorder list, we are able to build this tree in a nice way.

Also a tree is a recurrsive structure. So we can use a recursive function.

## algorithm

```pseudo
build_tree(preorder :[T], inorder :[T]) -> Tree[T]:
  
  if preorder is empty or inorder is empty:
    return NULL
  
  root := Node(preorder.pop_first())
  inorder_left, inorder_right := slice inorder at the root.value w/o root.value
  root.left := build_tree(preorder, inorder_left)
  root.right := build_tree(preorder, inorder_right)
  return root
```

## extra

I want an array representation of the Tree, just to make the comparison easier.

```ascii art
    a
   / \
  b   c
 / \ / \
   e f 
-> (Null is representet as \0)
[a, b, c, \0, e, f, \0]
```

We can argue, if the last entry will be part of the List, but I say, it is better to represent the whole level, so the last entries can be empty.

To make it easy a dynamic array is used, that increases the allocated space by the amount of the new level.
We can make conversion from a node based biTree to an array with a code like follows:

```pseudo
convert_bintree2array(tree :Tree[T])-> [T]
  array := dynamic array,automatically makes more space

  _fill_array(node :Node[T], idx :int):
    if node.value is empty: return
    if idx not in array range: double array size
    array[idx] = node.value
    _fill_array(node.left,  2*idx + 1)
    _fill_array(node.right, 2*idx + 2)
  
  _fill_array(tree.root, 0)
  return array  
```

Or we make use an array based Tree in the first place to construct the tree.
So we have to make a traversal through indices.
The a very simple specification of this, the tree can look like, without validation and bubbling up etc. Just the stupid dataholdingclass.

```pseudo
Tree[T]:
  - values :dynamic[T]
  + set_value(idx :int, value :T)
  + get_left(root_idx :int) :int
  + get_right(root_idx :int) :int
  ...

  + get_value(idx) :T
  + travers_so_and_so() :[T] or iterator
```

So the whole code will be looking like this:
For the better understanding, I will use an Iterator to keep track of the current entry preorder!
To make it more lowlevel, the slices can be represented as a starting and ending indices tuple. I will pass on this to not confuse more.

```pseudo
build_tree(preorder :[T], inorder :[T]) -> Tree[T]:
  if preorder.size != inorder.size : throw error
  preorder_it = make Iterator for preorder
  tree = new Tree[T]

  inner function: _build_tree(node: int, inorder_slice :[T]) -> void:
    if preorder_it has no next(): return
    value = preorder_it get next value

    inorder_idx = find value in inorder_slice 
    if value is not found in inorder: throw error
    inorder_left = slice inorder_slice from 0 to inorder_idx
    inorder_right = slice inorder_slice from inorder_idx to end

    tree.set_value(node, value)
    if inorder_left is not empty: _build_tree(tree.get_left(node), inorder_left)
    if inorder_right is not empty: _bulid_tree(tree.get_right(node), inorder_right)
  
  _build_tree(0, inorder)
  return tree
```

## extra for the dynamic array

dynamic array that increases the space by the next level:
I want to get the new size of an array by passing the old size into it.

```math
new_size(old_size) : int  ???
```

We now:

```math
first level = 0
extra level_space =  2**level

and

size = sum over all levels (2**level) = 2**(level+1) -1 # see numbers block below
```

writing a sequence of all sizes for the level 0 to 5:

```numbers
level : added extra space : total space
0 :  1 :  1
1 :  2 :  3
2 :  4 :  7
3 :  8 : 15
4 : 16 : 31
5 : 32 : 63
```

We see that the total space is `2**(level+1) -1`.

We can use the logarithm to get the level:

```math
size +1 = 2**(level +1)
-> 
level +1 = log_2(size+1)

level(size) = round up (log_2(size+1) -1) = round down (log_2(size+1))
```

But we can also simplify the equation to get rid of the logarithm.

We know, the array has always the size of a full binary tree with the specific level. so size is a function of level and vise versa. `size(level)^-1 = level(size)`. It stays in the interger space in both Sets and both Sets are of the same size.

```math
size = 2**(level+1) -1

old_size = 2**(old_level +1) -1 # known
new_size = 2**(new_level +1) -1

new_level = old_level+1

new_size = 2**(old_level + 1 + 1) -1
         = 2**(old_level + 1) * 2 -1
         = 2 * 2**(old_level +1) -1   # 2**(old_level +1) = old_size + 1
         = 2*(old_size+1) - 1
```

## python specific

i will use the dunder `__repr__() :str` to make the get.

[code](solution.py)
