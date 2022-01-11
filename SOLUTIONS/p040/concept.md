# find_non_duplicated(arr :[int], N :int=3) -> int

The simplest solution is to sort the array inplace, and search the only element, that is not in a group of three. Tat violates the linear time complexity: `O(N*log(N)) + O(N) > O(N)`.

I have to confess that I googled it. But the solution ist genius:
The algorithm is bit manipulation, bit counting , detecting with modulo and construction the value by set it up bit by bit.

It is not realy scalable, because we have to set the percition of the integers by a fixed value. For strong typed languages this is given by the integer type. In Python with no integer bounderies, we can check it by test the max value in the array against the fixed size, for example a `word= 4byte=32bit`.
Another approache, but that is no more `O(N)`, is to set the MSG bit to the `MSB` in the maximum value in the array.

## algorithm

`MSB=16` for a nibble.

1. non_dublicate = 0
2. for `n` in 0 ... `MSB`:
   1. `cnt_bit` = 0
   2. `bit` = make bitmask for the `n`th bit
   3. for each `value` in `array`:
      1. if `bit` is set in `value` (`bit & value`): `cnt_bit`++
   4. if `cnt_bit` is not dividable by `N` (`cnt_bit % N != 0`):
      1. set `bit` in `non_duplicate` (`non_duplicate |= bit`)
3. return `non_duplicate`

- space: `O(1)`
- time: `MSB * O(N) = O(N)`

## a more flexible but no more linear Time complexity

We can make `MSB` variable and search for it in the `array` up front.

```pseudo
find_msb(array :[int]) -> int
    maximum = maximum(array)
    return int(log2(maximum))
```

So this takes `O(N)` and for the rest it is `O(MSB*N)`.

If we allow negative values, we can assume, that the sign bit is the `MSB`.

For that, we can interpretate the value as an unsigned value and take search for the msb. A more robust algorithm, that allows negative integers.

```pseudo
find_msb(array :[int]) -> int
    msb = 0
    for each value in array:
       unsign_value = interpret value as unsign integer
       msb = max(msb, int(log2(unsign)))
    return msb
```

## I googled again

I found out that a python integer is on 64-bit systems also 64 bit long, by default. So the fixed version is 64.

But on my machine all negative integers got a set bit, if you check all higher bit positions. `(1<<32) & -1 == (1<<100) & -1 == True`.

By adding one, we can satifiy the `find_msb` algorithm and holding a sign bit.

if we construct this, we have to check the msb bit, that is the sign bit and convert the non_duplicate to a negative value.

[code](solution.py)
