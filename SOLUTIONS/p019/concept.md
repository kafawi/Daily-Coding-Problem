# Best Price for a Colorful Neighborhood

For a row of houses th minimum price for the color is needed.

## constrains

### No pair of direct neighbor has the same colored house

The number of colors `K` has to be more than `1`,
if number of houses `N` is greater than `1`.

### The houses are alined

It has a start and an end house with only one neighbour house.

### A house has directly an effect of its direct neigbours

The problem is sort of locally and minimum prices for a certain condition can be cached.
-> dynamic programming

## Input Data Formation

A $NxK$ matrix with priceses as elements of this definition:

- rows: `N` houses:
- cols: `K` colors:

## Go for an example

```pseudo
n = 4
k = 3
[     
 [ 1,  2,  3],
 [ 4,  5,  6],
 [ 7,  8,  9],
 [10, 11, 12],
]
```

Without constrains, we have $K^N$,
but with constrain and in a circle we have $(K-1)^N$,
but one time, we can chooe freely, because it is the beginning/ end and this got just one neighbour:$(K-1)^(N-1) * K$.

possiblie solutions : $(3-1)^(4-1)*3 = 2^3*3 = 8*3 = 24$

```pseudo
1 + 5 + 7 + 11 = 24
1 + 5 + 7 + 12 = 25
1 + 5 + 9 + 10 = 25
1 + 5 + 9 + 11 = 26
1 + 6 + 7 + 11 = 25
1 + 6 + 7 + 12 = 26
1 + 6 + 8 + 10 = 25
1 + 6 + 8 + 12 = 27
2 + 4 + 8 + 10 = 24
2 + 4 + 8 + 12 = 26
2 + 4 + 9 + 10 = 25
2 + 4 + 9 + 11 = 26
2 + 6 + 7 + 11 = 26
2 + 6 + 7 + 12 = 27
2 + 6 + 8 + 10 = 26
2 + 6 + 8 + 12 = 28
3 + 4 + 8 + 10 = 25
3 + 4 + 8 + 12 = 27
3 + 4 + 9 + 10 = 26
3 + 4 + 9 + 11 = 27
3 + 5 + 7 + 11 = 26
3 + 5 + 7 + 12 = 27 
3 + 5 + 9 + 10 = 27
3 + 5 + 9 + 11 = 28
```

This is very pricy.

Lets make a graph transition to see the recurrence

```pseudo
n: 0
  1 -> [5, 6] 
  2 -> [4, 6]
  3 -> [4, 5]

n: 1
  4 -> [8, 9]
  5 -> [7, 9]
  6 -> [7, 8]

n: 2
  7 -> [11, 12]
  8 -> [10, 12]
  9 -> [10, 11]

n: 3
 10 -> []
 11 -> []
 12 -> []
```

We can build a graph and find the lowest cost path. But that is too much for this problem. but from there we can take the locality.

I want to add the numbers together this time with a very simple algortihem, that is like a path finder.

```pseudo
n: 3
 10 -> 10 + 0
 11 -> 11 + 0 
 12 -> 12 + 0

n: 2
  7 -> 7 + path_min(11,12) = 7 + 11 = 18
  8 -> 8 + path_min(10,12) = 8 + 10 = 18
  9 -> 9 + path_min(10,11) = 9 + 10 = 19

n: 1
  4 -> 4 + path_min(8, 9) = 4 + 18 = 22
  5 -> 5 + path_min(7, 9) = 5 + 18 = 23
  6 -> 6 + path_min(7, 8) = 6 + 18 = 24

n: 0
  1 -> 1 + path_min(5, 6) = 1 + 23 = 24
  2 -> 2 + path_min(4, 6) = 2 + 22 = 24
  3 -> 3 + path_min(4, 5) = 3 + 22 = 25
```

It does not matter from which side of the road we start.

```pseudo
n: 0
  1 -> 1 + 0
  2 -> 2 + 0 
  3 -> 3 + 0

n: 1
  4 -> 4 + path_min(2, 3) = 4 + 2 = 6
  5 -> 5 + path_min(1, 3) = 5 + 1 = 6
  6 -> 6 + path_min(1, 2) = 6 + 1 = 7

n: 2
  7 -> 7 + path_min(5, 6) = 7 + 6 = 13
  8 -> 8 + path_min(4, 6) = 8 + 6 = 14
  9 -> 9 + path_min(4, 5) = 9 + 6 = 15

n: 3
 10 -> 10 + path_min(8, 9) = 10 + 14 = 24
 11 -> 11 + path_min(7, 9) = 11 + 13 = 24
 12 -> 12 + path_min(7, 8) = 12 + 13 = 25
```

Because of the constrain, just one option per house/step is forbitten-> so we can just store the two minima paths and what color number it has and forget drop the others.

### The algortihm in pseudo

```pseudo
min1, min2 = {0, -1}
for n=0; n<N; n++:
    local_min1, local_min2 = {infinity, -1}
    for k=0; k<K; k++:
        path_sum = matrix[n][k]
        if k != min1.index: path_sum += min1.value
        else: path_sum += min2.value
        if path_sum < local_min1:
            local_min2 = local_min1
            local_min1.value = path_sum
            local_min1.index = k
        elif path_sum < local_min2:
            local_min2.value = path_sum
            local_min2.index = k
    min1 = local_min1
    min2 = local_min2
return min1.value
```

[code](solution.py)
