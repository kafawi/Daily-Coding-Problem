This sounds like a tree structure i heard of: the Trie or something like that

The structure like this looks like a tree, that first vertice has all possible edges with an associated character (first character in a string of every entry in the dict.)
Every Vertex has a terminated state, to determin if the path from the root to this vertex is already an entry.

let us see what kind of thee we get, if we buld it word by word

a vertex is reperentedby () and a terminated vertex is (.)
an edge is represented as a line `- \ | etc...` the character is set between at least 2 lines `- a -`

```
()

fox:
()--f--()--o--()--x--(.)

face:
()--f--()--o--()--x--(.)
        \
         \-a--()--c--()--e--(.)

foxy:
()--f--()--0--()--x--(.)--y--(.)
        \
         \-a--()--c--()--e--(.)
```

After that is constructed, we can reTRIEeve very fast all possiblities for a given word in a recurrent manner.
We will use the chars as keys for the child dictionary `{char : Node}`, so we dont need an extra edge structur


in very vage pseudocode:
```
get_autocomplete_list(s :string) -> [string]:
    bucket :[string] = List()
    node = get the node in the Trie where s ends:
    if node exists:
       for every termination in every branch fill the bucket with the corresponding string
    return bucket
```

```
struct Trie:
  struct Node:
    is_terminated_ :bool
    child_paths_ :dict(char : Node)

  root_ :Node = {false, dict()}

  add_phrase(phrase: string):
    node :Node = root_
    for c in phrase:
      if c not in child_paths_.keys():
        next_node :Node = {false, []} 
        node.child_paths_.add(c, next_node)
      node = node.child_paths_.get(c).next_
    node.is_terminated_ = true

  get_all_phrase_(start: string, bucket :[string]):
    # we will use a Stack for this. 
    Stack : [Node] = []
    node :Node = root_

  get_node(phrase: string, pos: int):
    node :Node = root_
    for c in phrase:
        if c is not in node.child_paths_:
          return NULL
        node = node.child_paths_.get(c)
    return node

  travers_preorder(node: Node, prefix :string, fn: callable(node: Node, s: string)) :
    fn(node, prefix)
    for ch, child in node.child_paths_:
      travers_preorder(child, s + ch, fn)


struct autocompleteSystem:
    trie_ :Trie

    init(dictionary: Set[string]):
      trie_ = Trie()
      for entry in dictionary:
        trie_.add_phrase(entry)

    get_autocomplete_list(s :string) -> [string]:
        bucket :[string] = List()
        node :Node = trie.root_

        for c in s:
          if c is in node.child_paths_:
            node = node.child_paths_[c]

        sub_trie :Node = get_node(s);  
        if sub_trie is not NULL:
          travers_preorder(sub_trie, s[s.length-1], f(n, s) -> { if n.is_terminated_ : bucket.add(s)})
        
        return bucket
```


[code](solution.py)