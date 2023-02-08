# shuffle(array: [T]) -> void

We want to shuffle an array totaly randomly by only using swaps. All possible solution have the same propability -> unify distribution. We got a perfectl random funtion `rand_int(k :int) -> element in [1,k] : int`.

I assume the algorithm should be in-place, because the use of the swap operation only.

The time complexity should be `O(N)`.

## First thought

How do we get the unified distribution of all `N!` permutation? -> So each permutation has a propability of `1/N!`.

If we think of the lottery: The model is like a bin of nuberd balls, and the probability is raising for each ball to be choosen when a ball was choosen before, because the pool of competing balls shrinks.
The propability of a sequence that is build by this feels like a factorial operation.

Let's have an example: We have a pool of `N = 4` balls (let $p_i$ be the propapility of the $i$th permutation):
With our thinking before, the propability should be $p_i = 1/N$
\[
  p_i = 1/(4-0) \cdot 1/(4-1) \cdot 1/(4-2) \cdot 1/(4-3) = 1/4 \cdot 1/3 \cdot 1/2 \cdot 1/1 = 1/4! = 1/N!
\]

We can omit the last pick in our permutation, because swaping with itself does nothing.

I assume, my thoughts were correct, so let us build the algorith.

## algorithm

Time sould have to be `O(N)`. So we can walk through the array a constant number of time, so just one loop and no recursion inside!

For each place in the array, we pick a random card, represented by the index.
We swap place with the current card on that place with the picked indexed card.
with every place, we reduce the number of indexes, we can choose from, because our pool of cards decreases by every swap.

To imagin, we pick a card, and throw the old placeholder back in the bin bucket.

```pseudo
for i in [0..N-1]:
  picked_card_idx = random index between [i..N[
  swap entries of i and picked_card_index in the array
```

Next, let us fill the places of the array from the back to front, to reduce the confusion of to much arithmetic.

```pseudo
shuffle(array: [T]) -> void
  for i in [N-1..0[:
    picked_card_index = random index between [0..i]
    # swap
    tmp = array[i]
    array[i] = array[picked_card_index]
    array[picked_card_index] = tmp
```

We have to becareful with the strange range of the given randomfunction. So to use it as an index in a first-is-zero based world, we have to subtract the offset.

## how to test

For this, i will only test, if every card is in the shuffeld deck.

For a statistic test I would run the funktion about `M*N!` and for each permutation, a number count increases. In the end, all number counts should be round about the same number `M +- epsilon`, an error that I tollerate. But how to choose `M` and `epsilon`? I don't know actually. One thing is for sure: `M ~ 1/epsilon`. So I would choos a very big `M > N` and an `epsilon = M/N`. But I will pass the statistic test.

But we can test if all permutaions are met, when we run the function dozons of times.

[code](solution.py)
