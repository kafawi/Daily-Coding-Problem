# Find Minimum Number of Rooms

We have a list of periodes for a room use.

We can get the minimum number of rooms by finding the maximum of overlapps for every period?

## fist let us get a better picture of the problem by example

```pseudo
input: [(30, 75), (0, 50), (60, 150)]

t: 000 010 020 030 040 050 060 070 080 090 100 110 120 130 140 150
0               ...................
1   .....................
2                           .....................................

rooms: 2
0               ...................
1  .....................    .....................................    
------------------------------------------------------------------
input: [(0,1),(0,4),(1,2),(7,9),(3,6),(5,8)]
t: 0 1 2 3 4 5 6 7 8 9
0  ..
1  ........
2    ..
3                ....
4        ......
5            ......

rooms: 2
0  ....  ......  ....
1  ................
```

## simple solution

One solution is to check for every moment in time in the range how many lectures are happening:
If a period / lecture starts, we can increase a counter, if a period ends, we can decrease it. The max of the lecture counter will be the minimum number of needed rooms.

```pseudo
input: [(0,1),(0,4),(1,2),(7,9),(3,6),(5,8)]
t: 0 1 2 3 4 5 6 7 8 9
0  ..
1  ........
2    ..
3                ....
4        ......
5            ......

+  2 1 0 1 0 1 0 1 0 0
-  0 1 1 0 1 0 1 0 1 1
c: 2 2 1 2 1 2 1 2 1 0
-> max(c) = 2

with c for the counter of currently happening lectures
```

$ nlectures(t) = nlectures(t-1) + \Delta{lectures}(t)$
$\Delta{lectures}(t) = num(start(t)) - num(end(t))$

$nlectures(t_n) = \sum_{t=t_0}^{t_n} nstart_t - nend_t$

## But can we do it more efficient?

We dont have to step through every timestep. We can use an dictionary with a set of times as keys and a value, that determin how we manipulate the counter. $t \to \Delta{lectures}$

```pseudo
find_minimum_number_of_rooms(lecture_periods: [(start, end)]) -> int:

    time2delta_lectures : Dict = {}  

    for start, end in every period in lecture_periods:  # `O(n)`
        time2delta_lectures[start] += 1
        time2delta_lectures[end] -= 1
    
    
    delta_lectures = (sort(time2delta_lectures, using key time)).get_value_list()  # 'O(nlog(n))' 

    nlectures = 0
    min_rooms = 0
    for every delta_lecture in delta_lectures:     # `O(n+n) = O(n)`
        nlectures += delta_lecture
        # the minimum of needed rooms is determin by the maximum number of parrallel lectures
        min_rooms = max(min_rooms, nlecture)
    return min_rooms
```

The time complexity is $O(n + n\lg(n) + n) = O(n\lg(n))$
The space complexity is $O(2n + 2n + c) = O(n)$

[code](solution.py)
