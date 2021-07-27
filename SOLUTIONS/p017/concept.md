# Find the Longest Path of all Files in a File System

- file system is represented by a string.
- length is measured by number of characters.

## Notes

A File has a period `.` and a file extention.
A directory has neer an period.

## File System Representation

Every line is one file system item - file or directory.
The number of prefixed tabs indicatet the depth of the file system tree.
If the number of tabs is higher than one above, this item is inside the nearest prevous item - here directory, if file this file system is broken - that has one tab less.
There is a rule, that is nessessary. **A file can not contain an item!**

Also, every deep entry needs a directory, that is containing it, that apears befor that item!

But for the first take, we will just assume, that all representation are in a sound condition.

## First Algorithm

We can make this in `O(n) = n` because every context of any file is represented before in the string.

For the simplicity, we can first split the representation by the newline character `\n`.

And because the context is everytime retrospective we can use a stack to keep track of the parent directorys in the path.

Everytime we find a file, we can build easy a path and check, it the path string is longer than the one, we got before.

```pseudo
stack :List<string>
longest_path_length = 0
for every item in split(file_system_represenation, '\n'):
    # get the depth (number of tabs) and adjust the stack or 
    num_tabs = get_number_of_tabs(item) 
    # if num.tabs == stack.size : item is child
    for stack.size - num.tabs times:
        stack.pop()
    stack.add(item) 
    if item is file:
        length = 0
        for item in stack:
            length += item.length + size of the delimiter  # +1 for the simple /
        longest_path_length = max(length, longest_path_length)
    return longest_path_length 
```

## simplify the algorithm

because we just need the info for the length, and we are going naive and beliefe that the input is sound, we can store the length of the directorys in the stack.
We can also store the length of the total total path or the total path as a string in the stack.
The infomation is here redunand, but the complexcity is then `O(n)=n`. To keep a `O(n)=n` space, we store the length and not the total paths.

```pseudo
stack :List<int>
longest_path_length = 0
for every item in split(file_system_represenation, '\n'):
    # get the depth (number of tabs) and adjust the stack or 
    num_tabs = get_number_of_tabs(item) 
    for stack.size - num.tabs times:
        stack.pop()
    stack.add(stack.peek() + item[num_tabs:].length)  # here is a number out of bound possible
    if item is file:
        longest_path_length = max(stack.peek(), longest_path_length)
    return longest_path_length 
```

A robust version is to avoid number out of bounds:

```pseudo
stack :List<int>
stack.add(0)
longest_path_length = 0
for every item in split(file_system_represenation, '\n'):

    num_tabs = get_number_of_tabs(item) 
    for (stack.size - 1) - num.tabs times:
        stack.pop()
    stack.add(stack.peek() + item[num_tabs:].length + delimiter.size)

    if item is file:
        longest_path_length = max(stack.peek(), longest_path_length)
    return longest_path_length
```

`delimiter = '/'` so: `delimiter.size = 1`

### side note

we have to remove the size of one delimiter of the longest path, because there is no traling `/` padding delimiter, not like in other OS systems, like unix with the root '/'.

## What is with not so robust inputs

We can check if `stack.size - num_tabs` is less than 0, then there is invalid case like:

```none
input:                      stack.size   num_tabs  check
dir                             0           0        0
    subdir                      1           1        0
            subsubsubdir        2           3       -1  -> invalid format
        subsubdir                
```

because `subsubsubdir` has no direct parent.

If we remove directly after determin the size of the path the file from the stack, we can determin, if the next entry trys to make a file his parent directory with the detection, we got above.

Or we just do not include files on to the stack. That is clearer and will solve the side note issue

```none
input:                       stack.size  num_tabs  check 
dir                               0         0        0
    subdir                        1         1        0
        file.ext                  2         2        0
            subfile.ext           2         3       -1  -> invalid format
```

These are very easy to implement. the solution will have this adjustments.

For the sake of simplicity, this pseudocode will not have the root stack input of `0`.

```pseudo
stack :List<int>
longest_path_length = 0
for every item in split(file_system_represenation, '\n'):

    num_tabs = get_number_of_tabs(item) 
    if 0 > stack.size - num_tabs: 
        raise error 
    
    for stack.size - num_tabs times:
        stack.pop()
    if item is directory:
        stack.add(stack.peek() + item[num_tabs:].length + delimiter.size)
    else if item is file:
        longest_path_length = max(stack.peek() + item[num_tabs:].length, longest_path_length)
    
    return longest_path_length
```

### other checks

The biggest issue is a missformed input string. There are some ways to check it.

If the item is a real item, -> this can be checkt by a `is_valid(item :string) -> Boolean` helper.
(Also the `is_file(item :string)` helper could be check more)

Also what is with padding whitespace other than `\t` and `\n`?

Another invalid input could be if 2 items in the same context have the same name.

For this solution I will ignore those cases.

[code](solution.py)
