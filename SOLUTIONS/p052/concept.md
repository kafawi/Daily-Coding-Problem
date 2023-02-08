# LRU Cache

Implement an LRU Cache.

```uml
LRU Cache
---------
---------
+ set(key : Hashable, value :any): void
+ get(key : Hashable) -> any or null
---------
```

All operations are with `O(N)=1` time.

## Datastructures

Hashmap that points to the entry in the Double Linked List.

A double linked list because

At the `head`, we put the last usage (by get) or a new one by `set`.

At the `tail`, we will pop the least reasently used element, wenn the key is a new one, when we use `set`.

this implementaion lives in the heap, so it is not so fast as if it lives on the stack. We can implement a version, where the values are living in an array on on the stack with annotatied value, with the indices of next and previous entry. So a array implementaon of the double linked list will be implemented as an extra treat for this exercise. We assume, that the cache will does not lose entries, so if it is filled, there will never be a free slot.

For the hash map, I will use the given structure by the std libraries. I will assume, that it is also an array implementaion. But if we will keep the cache totaly on the stack, we can implement the hashmap with an array, that behave in an hash collision by puting the key in the next free slot of the array. Google just said, it is called open addressing. This is not as good as ol'gud chaining, because to hande a remove in this open addressing, we have to keep looking for potential shifted entries, to copy the last found into the now free slot. With chaining, we can remove that entry easier, because linked list. Both run in the worst case with `O(N)=N`, so it does not matter much. In the end, I don't care, how the library I will use implements the hash table.
All in all I assume every operation is of the complexity `O(N)=1`, so worst case (all keys have the same hash)of `O(N)=N` is very rarly, because the std lib devs are way smarter and many more than me alone.

If I think about stack and heap, than in most languages, the array, that is hidden in the Datastructures will be allocated on the heap, because of the dynamic size `n` and unknown datatype. So in the end, just a very specific LRU can only live on the stack.

## Implementaion

### some unusual cases

#### What happen, if we set a key into the cache, that is already inside?

We just move this key to the most reasently used place (list.head) and update the value.

Make some test cases for this.

### Double linked

The datatype looks like this:
The most magic is here, because

```pseude
class DoubleLinkedArrayList:
  - data :[(value:any, prev:int, next: int)]
  - tail :int
  - head :int
  - size :int
  - capacity :int
  + push_front(value :any) :int
  + get_front() :any
  + update_front(value :any)
  + move_front(index :int)
```

The implemetaion is somthing like this:

```pseudo
push_front(value :any) :int
  if it is empty (head == null):
    data[size] = (value, -1, -1)
    head = size (==0)
    tail = size
    size +=1
  if it is not full (size != capacity):
    data[size] = (value, head, -1)
    data[head].next = size
    head = size
    size +=1
  else: 
  # replace the entry at tail, set new tail to old tails prev, set the head new, maipulate the old heads next
    to_replace = tail
    tail = data[to_replace].prev
    delete entry at data[to_replace]
    data[to_replace] = (value, head, -1)
    data[head].next = to_replace
    head = to_replace
  return head

get_front() :any
  return data[head]

update_front(value :any)
  data[head].value = value

move_front(index :int) 
    if head == index: retrun # nothing to do
    # else:
    prev = data[index].prev
    next = data[index].next
    data[prev].next = data[index].next
    if tail != index: 
      data[next].prev = prev
    data[head].prev = index
    head = index
    data[index]
```

### LRU

```pseudo
class LRUCache:
  - data_list : DoubleLinkedArrayList
  - key2index : hashTable 
  + get(key :Hashable) :any
  + set(key :Hashable, value :any)
```

```pseudo
get(key :Hashable) :any
  if key is not in key2index: return null
  # else
  index = key2index[key]
  data_list.move_front(index)
  return data_list.get_front()

set(key: Hashable, value :any)
  if the key in key2index:
    data_list.move_front(key2index[key])
    data_list.update_front(value)
  else:
    index = data_list.push_front(value)
    key2index[key] = index
```

## After thoughs

Maybe it is better to use an super simple Double Linked List, that does only primitiv stuff checks nothing also does not kick out by its own, because the complex logic should be in the LRU class.

Also another problem is, that we have to remove the key in the hashmap after droping it in favor of a new one! We can solve this, if we stare the key in the double linked list also!

The code will more look like this if we want to let the LRU is in charge of removing/replacing the tail:

```pseudo
DoubleLinkedArrayList:
  - data : [(key, value, prev, next)]
  + head
  + tail
  - size
  - capacity

  + is_full() :bool
  + update(index, key, value)
  + move_front(index)               # like bubble up, but strait to top
  + push_front(key, value) :int
  + get_tail() :int
  + get_value(index) :any
  + get_key(index) :hash


is_full() :bool
  return size == capacity

update(index, key, value)
  data[index].value = value
  data[index].key = key

move_front(index)
  prev = data[index].prev
  next = data[index].next
  if prev exist (capacity > prev >= 0):
    data[prev].next = next
  if next exist (capacity > next >= 0):
    data[next].prev = prev
  
  data[head].prev = index
  data[index].prev = -1
  data[index].next = head
  head = index

push_front(key, value)
  data[size] = (key, value, -1, head)
  data[head].prev = size
  head = size
  size += 1

get_value(index)
  return data[index].value

get_key(index)
  return data[index].key
```

and the LRU:

```pseudo
class LRUCache:
  - data_list : DoubleLinkedArrayList
  - key2index : hashTable 
  + get(key :Hashable) :any
  + set(key :Hashable, value :any)


get(key :Hashable) :any
  if key is not in key2index: return null
  # else
  index = key2index[key]
  data_list.move_front(index)
  return data_list.get_value(index)

set(key: Hashable, value :any)
  if the key in key2index:
    index = key2index[key]
    old_value = data_list.get_value(index)
    data_list.update(index, key, value)
    data_list.move_front(index)
    # remove old_value from memory or decrease ref count
  else:
    if data_list.is_full():
      index = data_list.get_tail()
      old_key = data_list.get_key(index)
      key2index.remove(old_key)
      old_value = data_list.get_value(index)
      data_list.update(index, key, value)
      data_list.move_front(index)
      # remove old_value from memory or decrease ref count
    else:
      index = data_list.push_front(key, value)
      key2index[key] = index
```

[code](solution.py)
