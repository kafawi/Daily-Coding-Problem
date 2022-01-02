# get_capacity_of_valleys(profile: [int]) -> int

As input we got an array of integers, that you can interprete as a 2D raised-relief map or elevation profile of a terrain. With this analogie we have to calculate the max capacity or volume of all valleys. So the return value is the amount of water, that is hold by the terrains valleys, if its rains non-stop.
A valley is defined by a minima enclosed by two maximas of the discrete funtion defined by the input array.
The water can run off to both sides.

## complexity requirment

- time: `O(N)`
- space: `O(1)`

Because of the requirments I assume that there is a well-known solution.

## interesstinct problems

- a big vally contains more smaller valleys: `[2010103] -> 2+1+2+1+2 = 8`
- a slope: `[3210] -> 0`, `[0115]-> 0`
- a plateau: `[0122210] -> 0`
- a valley with a high peak in the middle: `[21302] -> 1+2 = 3`

## my algorithms

### First try

To understand the problem more.

```text
collect all maxima

compare the maxima and make pairs of valley

for these pairs collect the volume: 
  sum min(pair)-i for each i in arr between these pair

retrun the sum of these volume.
```

How to find a maximum: (it is some how state based, function theorie-ish)

- if the slope is raising: aproaching a maximum,
- if it is falling, the previous element is a maximum.

By padding a zero to head and tail, we can make it easier for us to find a maximum.

The complexity of space is not `O(1)` because the collection of maxima is `O(N)`.

## Another approach

How do we know, that a section of the array is filled to its fullest? We know, that the edges (head and tail) are run offs, in the analogy like a drain. So If we find the first maxima of one side, we know, that this maxima is a boundery for the water trap.
If we find the next maxima, that is taller or of the same height than the first, we have an other barrier for the water, and valley between the first and this maxima can hold at most water like:
`first_maximum_height * distance(first_maximum, second_maximum) - all hights in between`

or

```text
volume = 0
for each height between first and second maxima:
  volume += min(first_maximum, second_maximum) - height
```

And with our definition is `min(first_maximum, second_maximum) = first_maximum`

After we found one valley with `second_maximum >= first_maximum`, we can set the `first_maximum = second_maximum` and do the same as before, till we reach the end of the profile.

If we find no more `second_maximum` that is `second_maximum >= first_maximum` we can run the same algorithm from the other side till the last position of `first_maximum` from the first run. The result is the sum of all those valley capacity.

I short, we search for valley, defined by two bonderies. The first is a maximum, the second is a raising slope or another maxima, which is of the same height or higher like the first.

We can do it in a state like designe with 2 states:

1. searching for maximum
2. searching for the opposite boundery

if we are in the `searching for maximum` state, and find a maximum, we have a transition in which we remember the this position and change the state to `searching for the opposite boundery`. If we find a boundery, we sum up the differences into the capoacity value and change the state back to `search for maximum`.

Because we have just 2 states, we will use a boolean to identify the state:

1. `in_valley = False`: searching for maximum
2. `in_valley = True`: searching for the opposite boundery

### as pseudocode

Because we run almost the same algorithm but with different directions and in the second run eventually with an sooner stop index, the code looks a little redundant.

```text
get_capacity_of_valleys(profile: [int]) -> int
  capacity = 0
  maximum = -1
  in_valley = False
  for (i=1; i <profile.length; i++>):
    if in_valley: searching for the opposite boundery
      if profile[i] >= profile[maximum]:
        capacity += sum all profile[maximum] - profile[j] for each j between maximum and i 
        in_valley = False
    else:#  searching for maximum
      if profile[i-1] > profile[i]:
        maximum = i-1
        in_vally = True
  # backwards if in_valley is true 
  if in_valley:
    in_vally = False
    stop = maximum  
    for (i=profile.length-2; i >= stop; i-->):
    if in_valley: searching for the opposite boundery
      if profile[i] >= profile[maximum]:
        capacity += sum all profile[maximum] - profile[j] for each j between maximum and i 
        in_valley = False
    else:#  searching for maximum
      if profile[i+1] > profile[i]:
        maximum = i+1
        in_vally = True
  return capacity
```

### complexity

- time: `3*O(N) -> O(N)`
  - in the worst case, we search for the maxima one time from the left and one time from the right -> `O(N) + O(N) = 2*O(N)`
  - by collectin the capacity, we run each vally one time minus the maxima -> `O(N)`

- space: because we have a costant number of variables independent of the length of the input -> `O(1)`

## after thoughts

We can refactor the redundant code to make it a little smoother, by defining a function. Also we use a vally buffer for the capacity for each potential vally, so we do not have to iterate an extra round fo sum up the capacity for each valley.

[code](solution.py)
