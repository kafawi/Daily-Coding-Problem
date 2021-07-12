The freedom here is the representation of how the serialized representation looks like. 

first: define the syntax of our function:
```
serialize:(root:Node) -> String
deserialize:(s:String) -> Node (root of the tree)
```
For the sake of simplicity, let us narrow the value type to String, so we have not to store a type value. 

by using the given Node class, let us define a representation of one node, as a recurrent structure:

```
("<val:String>";<left:Node>;<right:Node>)
```

- A Node entity is enclosed by parentheses
- the value is enclosed by quotes (just string)
- the Node Members are separated by semicolon `;` in the order val;left;right


### serialize
let the power of recursion begin... (to lazy to do it iterativ)
-> If the node is `null / None` an empty string is returned.
 If the Value is `null / None`, let the val position empty without quotes, to distinguish between `"None"` and `None` and an empty String. 

```
serialize(root:Node) -> String:
   if root is None: return ""; // terminate the recursion
   val_str: String = "" if root.val is None else "\"" + root.val + "\""
   left_str: String = serialize(root.left)
   right_str: String = serialize(root.right)
   return "("+ val_str +";"+ left_str +";"+ rigth_str +")"
```

### deserialize 
the power of regEx

- if the format does not match, an FormatException is raised.
- if trailing space characters are allowed, to make it more robust. 
```
deserialize(s:String) -> Node:
   // test if format fits (starting and ending parentheses or empty)
   if it does not match: raise Exception
   if s is empty: return None  // terminate the recursion
   
   // extract the fields and parse them with catch groupes, strip them!
   val:String = remove the quotes from val_groupe if it is not empty, else None
   left:Node = deserialize(left_group)
   right:Node = deserialize(right_groupe)  

   return new Node(val, left, right) 
```

Let's use python, because the node class, and a test case is already given to us in this language.


language: python
[code](solution.py)

for the tests:
run `python solution.py`

There is on complain in my implementation, that I don't like:

The regEx for the value is does not allow quotes, but `".*"` is too greedy. 

A better and easier way is to stringify it via json.
-> json needs dictionaries, so let us implement the recursion logic in helping functions

[code with json](solution_json.py)

following thoughts for future me:
- if we want to store other "primitive" types, we can do like in a json representation
- if we want to allow every type, we can store the type value before or after the `value`.
- if the tree has a static type, we can declare it at a meta prefix. 
- with subtypes is another complexity, so I stop to discuss

run `python solution_json.py`
