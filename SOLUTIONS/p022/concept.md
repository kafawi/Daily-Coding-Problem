# Find a Original Sentence

```pseudo
find_original_sentence(dictionary: {string}, nospace_sentence: string) -> {null, [string]}
```

## we use the power of recursion

`find_original_sentence(dictionary: {string}, nospace_sentence: string) -> {null, [string]}`

1. if nospace_sentence is empty: return empty list
2. list = null
3. for each word in dicionary:
    1. list = null
    2. if nospace_sentence starts with word:
        1. list = find_original_sentence(dictionary, nospace_sentence without word at the beginning)
        2. if list not `null`:
            1. insert `word` at the front of `list`
            2. break
4. return list

## How deep we want to go?

This algorithm is not very efficent, if we do not optimize the underlying datastructures $O(n^m)$ with $n$ af number of words in the dictionary and $m$ the aproximated number of words in the sentence or the to simplify the number of characters in the sentence.

If this is too slow, for every algorithm. We could go deeper and can optimize:

- by using indexing instead of every time new instanziation of a new String. Or for example using in *Java* structures like a `StringBuilder`.
- using a Trie as dictionary, to get faster less matching words. (This will make the most effect.)
- not using recursion, but a self organized stack of the words and positions
- using a double linked list

For this problem, I would use the highest level abstraction of the used programming language.

## Others

### preconditions

- `dictionary` is not empty
- `nospace_sentence` is not `null`

### special cases

- if `nospace_sentence` is empty, an empty `list` is returned
- if `dictionary` contains an empty string -> remove this entry

[code](solution.py)
