# randN()-> `0..N` with randM() -> `0..M`

The solution to this problem is to find the formular.

If the inner random function provides a uniformed distribution of `0..M`, than how and how many times must we roll this function to get a uniformed distribution of `0..N`.

but first , let us define random function:

```math
\text{rand} : \mathbb{N} \times \mathbb{N} → \mathbb{N}, (a, b) \mapsto \text{rand}(a,b) := \text n \in [a, b] \\

\forall n : \text{propability } p_n = \frac{1}{N} \text{with } N:= b-a+1
```

## idea: mean

```math
rand(a,b)= \frac{\sum_{i=0}^{N} rand(c,d)}{M} \newline
\text{with } N := b-a+1 \text{ and } M :=d-c+1
```

But there is a big problem: THE RULE OF STATISTICS: A sum of distribution is going to be more like a normal distribution.

## idea: roll a combination, not a sum

It is easy to use a random generator, that produces a big discrete interval, to use it for a generation for a smaller discrete interval, when both are uniformed. Just roll again, till it fits.

```math
\forall N := b-a+1 < d-c+1 =:M \\

\text{rand}(a, b) =
\begin{cases}
    (\text{rand}(c, d) - c)+a &, \text{if } \text{rand}(c, d) - b < N \\
    \text{rand}(a,b)              &, \text{otherwise}
\end{cases}
```

If we roll a combination, we raise our interval by the times of rolls.

```math
R := \text{number of rolls}\\
\prod^R N = N^R, \qquad
\prod^R p_n = \frac{1}{N^R}
```

If we map this combination to a number, we can create a number bigger than the befor. If make a `M` based number system, we can create a number bigger or equal than `N`.

```math
comb = \sum_{i=0}^{R-1} (\text{rand}(c,d)-c)*M^i
```

If we know the size of `N` and `M`, we can also use the modulo operation, if the product of $F*N$ for the factor $F \in \mathbb{N}$ is the neraest to $M^R$.
So we can avoid multiple rolling.

## pseudo code

```pseudo

R := 1
while M^R < N:
  R++
F = 1
while (F+1)*N <= M^R:
  F++

do
  n := 0
  for i in 1..R:
    n += (rand(c,d) -c)*(M^i)  
while n >= F*N

return (n mod N) + a
```

But we know `a,b,N` and `c,d,M`. So we can be concrete:

```math
a=1, b=7 \to N = 7 \\
c=1, d=5 \to M = 5 \\

R = 2: \quad M^{R-1} = 5^1 = 5 < 7 = N \quad M^R = 5^2 = 25 \geq 7 = N \\
F = 3: \quad F*N = 3*7 = 21 \leq 25 = M^R \quad (F+1)*N = 4*7 = 28 > 25 = M^R \\

\text{rand}7() := \text{rand}(a,b) = rand(1,7) \qquad \text{rand}5() := \text{rand}(c,d) = rand(1,5)  
```

long story short, this is a very complicated way to solve for a very simple solution.

```pseudo
rand7()-> int:
  do
    n = (rand5()-1)*5 + rand5()-1
  while(n < 21)
  return (n mod 7) + 1
```

[code](solution.py)
