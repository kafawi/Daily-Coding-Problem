This problem is a very nice problem, that I want to solve in C or C++.

```
class XorLinkedList<T>:
   class Node<T>:
     + value: T
     - both: POINTER
  
  - head: POINTER<Node<T>>
  - tail: POINTER<Note<T>>
  - size: int
  
  + add(element: T) : void
  + get(index: int) : Node_ptr  (better just the value of type T)
```

### How do we get the linked pointers from the `both` field

lets go by example:

```
next = 01
prev = 10
both = 01 xor 10 = 11

-> both xor next = 11 xor 01 = 10 = prev
-> both xor prev = 11 xor 10 = 01 = next 

null = 00 -> wenn both == prev -> there is no next and vise versa 
```

The following should give us a better understanding
```
addr:             001     100     010
node.both: 000 <-[100]<->[011]<->[100]-> 000
```

we need to use the opposite pointer to get the other.
### How to traverse?
If we want to traverse forward, we have to store the `prev` every step...

in pseudo code for forward, note the nodes variables are all pointer, and the arrow is used like in `C`.
```
node = List.head
prev = null_ptr
while (node != null_ptr):
    // do somthing with node->value
    next = node->both xor prev 
    prev = node
    node = next
```
for backwards just swap the `prev` with the `next` variable.

### Design the methods
Adding an element at the end
```
add(element: T) : void:
  node = get_pointer(create_Node(T))
  if size == 0:
    node->both = null_ptr
    head = node
    tail = node
  else:
    prev = tail
    prev.both = prev.both xor node // prev.both == prev.prev xor null_ptr == prev.prev
    node.both = prev // null_ptr xor prev == prev 
    tail = node
  size++
  return
```
We are not "smart" here and always traverse forward..., the backward run is similar
```
get(index: int) : Node_ptr:
  if not (0 <= index < size):
    raise Exception
  
  node = head
  prev = null_ptr
  for i=0; i < index; i++:
    next = node->both xor prev
    prev = node
    node = next
  return node
```
For a robust design: `get(index)` not return a Node reference but just its value. I will it implement this way! 

let us use `c++` for this implementaion:

[code](xor_linked_list.h)  
[test](xor_linked_list_test.cc)

Run in the terminal to compile and run the tests (here with my favorit `clang` compiler):

`clang++ xor_linked_list_test.cc && ./a.out -l all`

(You will need the `boost` lib to compile)


### After thoughts:
That took me too long, but I learnd:
- boost test framework
- get in touch with the cpp stuff again.
  - the logic was super fast but the cpp extra steps are more time consuming.
  - `friend` are such a interesting concept, that is somtimes hard to understand.
  - understanding `templates` in cpp but not fully -> so the implementation is in the header ...
  - style guides are too detailed to crawl fast through...
  - i am too lazy to install and run an IDE for c/cpp but maybe next time

What to discuss further is the allocation and deallocation of its values Should the list use the move command or does the nodes hold just a reference / smart pointer? It depends on the use case. 
Docstrings and documentation is missing. A private `get_node(int index)` could be handy for further tests. A Method `Node.get_other_link(Note_ptr link) -> Note_ptr: return both_ ^ link;` or a function `xor(void* a, void* b)-> void*`, that hides the wild casting could make the code more readable. Also what is with other architectures like 32-, 64-, 128-bit.git 
