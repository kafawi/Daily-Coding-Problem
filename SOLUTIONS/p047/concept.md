# calc_maximum_profit(stock_price_history :[DOLLAR]) -> DOLLAR

the problem is more of reduced o the mathematical search for each minimum and a following maximum. By searching for such pairs in one pass, we can remember the biggest difference, that is also our maximum profit, that we return.

A much more and easy approache, is to search for each price the differnce to the following and return the maximum.

## algorithm

```pseudo
calc_maximum_profit(stock_price_history :[DOLLAR]) -> DOLLAR
maximum_profit = -infinity
for t0 in 0 .. length(stock_price_history)-1:
  for t1 in t0+1 .. length(stock_price_history):
    profit = stock_price_history[t1] - stock_price_history[t0]
    if maximum_profit < profit: 
      maximum_profit = profit
return maximum_profit
```

### thoughts

Can we optimize it from this `O(N^2)` to better one?

We can do it in `O(N)` by remebering the minimum and the maximum_profit.

That is possible, because of the minimum is just resonsable for the prices ahead of itself. So we can forget about the maxima in the past.

In other words, if the global minimum is befor the global maximum : the max profit is `maximum - minimum`.
You can find the maximum profit, if you see the minima and maxima in relation to another.

I more accurate definition, if you invest in time = t, than the maximum profit is defind as:
maximum_profit(t) = global maximum from time < t.

I have a hard time to explain it in words, so let us explain it through code

## better algorithm

```pseudo
calc_maximum_profit(stock_price_history :[DOLLAR]) -> DOLLAR
    maximum_profit := -infinity
    minimum_price := stock_price_history[0]
    for each price in stock_price_histoy starting at second entry:
        if maximum_profit < price - minimum_price:  maximum_profit := price - minimum_price
        if minimum_price > price: minimum_price := price
    return maximum_profit
```

[code](solution.py)
