# modern alcemist: is_possible_arbitrage(currency_exchange_rates :\[[float]])

We are a possibe fraud detector and have to validate an exchange rate table for different currencies if there is a possiblility, that by exchanging from a starting currency, is there a way to get an extra amount for free if we exchange to other currencies and than back to the starting one.

## How does the 2D tabel looks

The exchange rate matirx has the dimention `N`x`N` and
`N` is the number of different currencies. The first dimension is the `from` and the second is the `to` dimension.

The type could be fix point values, that are more robust than normal floating point values, because the precision is on point (badum tshhh). With normal floating point we have the problem with a conversion from float to int and the internal representation error.

Example for a whole matrix

```text
    USD         EUR         YEN
USD   1           0.885604  116.138113
EUR   1.129173    1         131.127827
YEN   0.008610    0.007626    1
```

## How do we can make money for free?

We can represent this matrix as a fully connected graph, where the currencies  are the vertices `v[i]` and the rates are the weights of the edges `e[i,j].weight -> rate of a exchange from currrency i to currency j`. With that interpretation we can say: `currency_exchange_rates[i,j] = e[i,j].weight` for all `i,j in [0..N]`

A more mathematical formal definition:

- Let `V` be all vertices each represent a currencies, with the size of `N`.
- Let `E` be all Edges each represent an exchange from currencies to another with the size of `N`x`N`size.
- Let `E[v,w].r` represent the rate of a exchange from currency `v` to `w`.

For an impossible arbitrage table following rules are nessecary:

```math
1.\quad e_{vw}.r = e_{wv}.r^{-1} \qquad\\
2.\quad e_{vx}.r = e_{vw}.r \cdot e_{wx}.r \\
\forall v,w,x \in V \quad \textrm {and} \quad \forall e \in E
```

if we look closer, the first rule is included by the second, because:

```math
\quad 1 = e_{vv}.r \overset{(2)}{=} e_{vw}.r \cdot e_{wv}.r \overset{(1)}{=} e_{vw}.r \cdot e_{vw}.r^{-1} = 1
```

By validate all path from one currency to all others and find out, that one part differs in the product of rates to the others. Or in other words, is there a cycle, that netto rate is < 1, so we can cylcle it many times.

## How can we find a negativ Cycle

Example the matrix:

We can make it very timeconsuming with an `O(N!)` algorithm, that is brute forced but robust.

For every combinaiton of exchanges, we finally exchange back to the origin and we look at the difference of the origin start value. If there is any (too much) difference, we can say, jepp, this is a bad exchange tabel.

But `O(N!)` is never good.

## So I google

If we are just interested in the case, that we kan make money out of it, we can search for the shortest path and, check if that shortest has a cycle, that is negative. By shortest, i mean the lowest produt of the rates.

We could use the logarithm to transform the rates in to a additive weight.

```math
e_{vw}.r = e_{wv}.r^{-1} \iff \log(e_{vw}.r) = -\log(e_{wv})
```

But we also could use the multiplikation instead of the addition in an path finding algorithm.

The Bellman-Ford pathfinding algorithm can find a negaitv cycle. If we found such a cycle, we detectet a possible arbitrage in the table. But we have to tweek the data a little bit, by inverting the values with the additiv method with the logarithm, or we change the logical operator to the opposite. So in both ways, we can imagin, that we flip the floting point number stream.

But why to flip the numbers: So we want at the end a little extra on top, by going back to the origin. We want to detect the path, that will give you a higher amount. But the Bellman-Ford can only detect the path with the lowest distance. By flipping we make the longest path the shortest.

If we want to detect, if the table is crooked in any way, we just have to find a path that differs from the others.

Time complexity is `O(n^3)`. That is much better than the faculty.

## Pseudo code

### Bellman-Ford variant

In general the addition version

For the sake of simplicity, we omit the shortest path graph variable.

```math
includes_negative_cycle(table: float[n,n], start :int) -> boolean:
    min_dist : [float] allocate of size n := {INFINITY}
    min_dist[start] = 0

    # because one degree of freedom was taken away by min_dist[start] = 0 we just to have relax n-1 times  
    for n-1 times:
    for v in 0...n:
      for w in 0...n:
        if min_dist[w] > min_dist[v] + table[v][w]:
          min_dist[w] = min_dist[v] + table[v][w]
    
    # by a additional run, nothing should change, except if a negative cycle is present
    for v in 0...n:
      for w in 0...n:
        if min_dist[w] > min_dist[v] + table[v][w]:
            return True
    return False
```

#### transformt version

```text
is_possible_arbitrage(currency_exchange_rates :[[float]]) -> boolean:

    # Flipping the table and change from multiplication to addition
    table : [[float]] allocate of size current_exchange_rates
    for v in 0...n:
      for w in 0...n:
        table[v,w] = -log(currency_exchange_rates[v,w])

    start = 0
    n = table.length
    min_dist : [float] allocate of size n := {INFINITY}
    min_dist[start] = 0

    # because one degree of freedom was taken away by min_dist[start] = 0 we just to have relax n-1 times  
    for n-1 times:
      for v in 0...n:
        for w in 0...n:
          if min_dist[w] > min_dist[v] + table[v][w]:
            min_dist[w] = min_dist[v] + table[v][w]
    
    # by a additional run, nothing should change, except if a negative cycle is present
    for v in 0...n:
      for w in 0...n:
        if min_dist[w] > min_dist[v] + table[v][w]:
            return True

    return False
```

#### flipped operator version

I don't know, if this is a valid way, because my guts are telling me, that this feels like the treveling salesman problem. Maybe I am lucky and it is valid, because the product mean of all rates is 1.

```text
is_possible_arbitrage(currency_exchange_rates :[[float]]) -> boolean:
    table = currency_exchange_rates 
    start = 0
    n = table.length
    
    max_dist : [float] allocate of size n := {0}  # multiplication lowest is 0
    max_dist[start] = 1   # init neutral number in multiplication is 1

    # because one degree of freedom was taken away by min_dist[start] = 1 we just to have relax n-1 times  
    for n-1 times:
      for v in 0...n:
        for w in 0...n:
          # hence the flippt operator
          if max_dist[w] < max_dist[v] * table[v][w]:
            max_dist[w] = max_dist[v] * table[v][w]
    
    # by a additional run, nothing should change, except if a "rate > 1" cycle is present
    for v in 0...n:
      for w in 0...n:
        if max_dist[w] < max_dist[v] * table[v][w]:
            return True

    return False
```

### just the check, if every path has the same rate

```text
is_possible_arbitrage(currency_exchange_rates :[[float]]) -> boolean:
    # init
    rates = copy currency_exchange_rates[0,:]
    for _ in range(n - 1):
      for v in 0...n:
        for w in 0...n:
          if rates[w] != rates[v] * currency_exchange_rates[v][w]:
            return True
    return False
```

[code](solution.py)
