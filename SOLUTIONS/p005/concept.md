This is looks like some pythons everything is an object thingi

Let's just frickle our way through

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

let's decrypt:

`cons` is a constructor that returns a function (pair) with one parameter, that looks like an abstract function `f` that is called, when pair is called.
This abstract function has its parameter already set to the arguments passed by `cons`, but the implementation is missing.

So my attempt is to pass the `pair(f)` a function, that satisfies the signature `f(a,b)`, so that the hidden arguments 
can be retrieved, by calling `pair` with this function.

```python
def comparableToPair(pair):
   def f(a,b):
      return ... # something with a and b
   return pair(f)
```

Lets us use this kind of syntax to create `cdr` and `car`:

```python
def car(pair):
   def f(a,b):
      return a
   return pair(f)

def cdr(pair):
   def f(a,b):
      return b
   return pair(f)
```

I will use lambdas to make it more readable:
[code](solution.py)

