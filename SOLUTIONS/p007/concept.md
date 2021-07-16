every time two digits decodes to a character, the one by one digit to char solution gets a brach to explore. 
This is a typical problem, that can be solved by recursion. 
So every time we hit the end of the seqence we return a 1, that adds up to the callers count value.
To start this recursion function with the recursion ending case thingi is in my opinion the best KISS.
We dont have to check for unvalid incomming messages. 

```python
count_possible_decodings(message :str) -> int:
    if message is empty:
        return 1
    # get every single position as one possible.
    num = count_possible_encoding[message[1:])
    # the possible 2 char branch adds one possiblility
    if message.length >= 2 and message[:2] <= encode('z'):
        num += count_possible_encoding(message[2:])
    return num
``` 

#### Other solutions:
 We coud do it also in a hybrid intertive, with recursion every time a possible brach is found.
 also we can do it iterative but that is not very readable, because we have to handle the stack by our own.