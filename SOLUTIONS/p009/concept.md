```
calc_largest_non_adjacent_sum(numbers :[int]): -> int
```

The first idea in a Sum of non-adjacent numbers in a List is, how do i manage the skips over mor than one number?
Is it a space independent problem, so if find the largest sum in the first half, and a largest sum in the second, the only critical place are the two numbers, that are touching when we connect the two lists?
Yes, it is like the this. so we need to keep track of just the last few entrys we visited, when we iterate through.
We can forget about the numbers before, and just remember the previous greates sum, and the sum, that was freshly made out of the current number and is forbitten for the next calculation.


If we assume a simple case, there are at least 2 positive non adjacent numbers in the array, we can initialize the two sums with the neutral element of the sum `= 0`
let us run an example wirth the following algorithm, so the values used are a function of the current index `index` in the loop over `numbers`, so we have not to keep track of swapping at this point
```
prev_sum(0) <- 0
max_sum(0) <- 0
for i<-0; i<numbers.length; i++:
   max_sum(i+1) <- (prev_sum(i) + numbers[i], max_sum(i))
   prev_sum(i+1) <- max_sum(i)

return max_sum(numbers.length)
```

If we rearrange an array like this for every step: `a(i):[int] = [prev_sum(i), max_sum(i)] + [numbers[i:]]`, we get following algorithm:
```
for i=0; i<numbers.length; i++:
  a(i+1)[1] <- max( a(i)[0]  + a(i)[2], a(i)[1])
  a(i+1)[0] <- a(i)[1] 
```
This will turn the array in following seqences with the examples of the problem description. It showes good the locality of the problem. `a' := a(i+1)`
```
i : a                   -> a'[1] <- (a[0]+a[2], a[1]) : a'[0] <- a[1] 
0 : 0, 0, 2, 4, 6, 2, 5 ->   2   <- ( 0  + 2  ,  0  ) :   0   <-  0 
1 : 0, 2, 4, 6, 2, 5    ->   4   <- ( 0  + 4  ,  2  ) :   2   <-  2
2 : 2, 4, 6, 2, 5       ->   8   <- ( 2  + 6  ,  4  ) :   4   <-  4
3 : 4, 8, 2, 5          ->   8   <- ( 4  + 2  ,  8  ) :   8   <-  8
4 : 8, 8, 5             ->  13   <- ( 8  + 5  ,  8  ) :   8   <-  8
5 : 8, 13

i : a                   -> a'[1] <- (a[0]+a[2], a[1]) : a'[0] <- a[1] 
0 : 0, 0, 5, 1, 1, 5    ->   5   <- ( 0  + 5  ,  0  ) :   0   <-  0 
1 : 0, 5, 4, 6, 2, 5    ->   5   <- ( 0  + 1  ,  5  ) :   5   <-  5
2 : 5, 5, 6, 2, 5       ->   6   <- ( 5  + 1  ,  5  ) :   5   <-  5
3 : 5, 6, 2, 5          ->  10   <- ( 5  + 5  ,  8  ) :   6   <-  6
4 : 6, 10               
```

The algorithm in pseudocode:
```
calc_largest_non_adjacent_sum(numbers :[int]): -> int:
  prev_sum: int = 0
  max_sum: int = 0
  for number in numbers:
    new_max_sum int: = (prev_sum + numbers, max_sum)
    prev_sum =  max_sum
    max_sum = new_max_sum
return max_sum
```

### Some case discussion
If we have just negativ numbers:
1. is the largest sum a sum of non member = 0 
2. a sum of one number = max(array)
3. or does a sum must have at least 2 inputs?

1. The first case is the easyest, becaus we initialize the variables with = 0
2. The second is a bit more complicate but it is accomplished with a search for the max in the array.
3. The third is much more complicated but we can do this, if we search for the three largest numbers with attatched index ("with a bounded priority queue") and than get the highest sum for non-adjacent.  

The complexity fo this could be:
1. one loop  -> `O(n)`
2. one loop for the normel run and another to get the max  -> `n + n = 2n -> O(n)`
3. one loop and another for the priority queue run -> `n + k*n = n + 3n = 4n -> O(n)`

So for the complexity it doesn't matter how we define our sum. 

The implementaion for this are
1. the default `calc_largest_non_adjacent_sum`
2. `calc_largest_non_adjacent_sum2`
3. `calc_largest_non_adjacent_sum3`

[code](solution.py)