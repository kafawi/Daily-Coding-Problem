# calculate_number_of_queen_arrangement(N: number of queens and size of board) -> int

So because the board is `N`x`N` and there are `N`  queens to place and a queen occupies its row and coulum comlpletly, There a for each row or column at most one queen. -> the last queens cell is fully determined by all others.

So we can iterate through ech row on the board. and if one cell is fee in the last row, we have a valid arrangement.
Also, with each queen placed, the degree of freedom decreases for the other rows / queens.

## Make some examples

- `Q` is queen
- `x` is not free
- `.` is free

```text
N = 1
Q -> 1

N = 2
Qx
xx 
-- -> 0

N = 3
Qxx Qxx Qxx
xx. xxQ xxQ
x.x xxx --- 0

xQx
xxx
.x. 0

0 arrangements

N = 4
Qxxx Qxxx   
xx.. xxQx 
x.x. ---- 
x..x x.xx

     Qxxx Qxxx
     xxxQ xxxQ
     x.xx xQxx
     xx.x ----

xQxx xQxx xQxx xQxx  
xxx. xxxQ xxxQ xxxQ
.x.x .xxx Qxxx Qxxx
.x.. xx.x xx.x xxQx -> symetrie 2

2 arrangements
------------------------------------

N = 5
Qxxxx Qxxxx Qxxxx Qxxxx Qxxxx
xx... xxQxx xxQxx xxQxx xxQxx
x.x.. xxxx. xxxxQ xxxxQ xxxxQ
x..x. x.xxx x.xxx xQxxx xQxxx
x...x x.x.x x.x.x xxx.x xxxQx  -> 2

      Qxxxx Qxxxx Qxxxx Qxxxx
      xxxQx xxxQx xxxQx xxxQx
      x.xxx xQxxx xQxxx xQxxx
      xx.x. xxxx. xxxxQ xxxxQ
      x..xx xx.xx xx.xx xxQxx -> 2

      Qxxxx Qxxxx 
      xxxxQ xxxxQ 
      x.xxx xQxxx 
      xx.xx ----- 
      x..xx xx.xx             -> 0


xQxxx xQxxx xQxxx xQxxx xQxxx
xxx.. xxxQx xxxQx xxxQx xxxQx
.x.x. .xxxx Qxxxx Qxxxx Qxxxx
.x..x .x.x. xx.xx xxQxx xxQxx
.x... xx.x. xxxx. xxxx. xxxxQ  -> 2

      xQxxx xQxxx xQxxx 
      xxxxQ xxxxQ xxxxQ 
      .x.xx Qxxxx Qxxxx 
      .xx.x xxx.x xxxQx 
      .x..x xxx.x -----       -> 0

            xQxxx xQxxx xQxxx
            xxxxQ xxxxQ xxxxQ
            xxQxx xxQxx xxQxx
            .xxxx Qxxxx Qxxxx
            xxx.x xxx.x xxxQx  -> 2

xxQxx xxQxx xxQxx xxQxx xxQxx
.xxx. Qxxxx Qxxxx Qxxxx Qxxxx
x.x.x xxx.x xxxQx xxxQx xxxQx
..x.. x.x.. x.xxx xQxxx xQxxx
..x.. x.xx. xxxx. xxxx. xxxxQ  -> symetrie 2
```

```text
conclusion:
N : number of arrangements
1 :  1
2 :  0
3 :  0
4 :  2
5 : 10
```

So if a mathematical formaular exist, than it is something like:

```math
f(N) = 
\begin{cases}
    1 &   N = 1 \\
    0 & N \in \{2,3\} \\
    f'(N)=? & N > 3  
\end{cases}
```

but I doubt it.

## an algorithm, brut force

```pseudo
f(N: int, y :int, queen_y2x:[int]) -> int:
    if y == N: return 1
    arrangements = 0
    for each x in free_x(N, y, queen_y2x):
       queen_y2x[y] = x
       arrangements += f(N, y+1, queen_y2x)
    return arrangements

free_x(N: int, Y: int, queen_y2x: [int])-> List[int]:
    x_occupie_count = [0]*N
    for y in 0...Y:
        x = queen_y2x[y]
        # vertical
        x_occupie_count[x] += 1
        # diagonal
        dx = Y-y
        x_occupie_count[x-dx] += 1
        x_occupie_count[x+dx] += 1
    
    free_x = List()
    for x, count in enumerate(x_occupie_count):
        if count == 0:
            free_x.add(x)
    return free_x
```

[code](solution.py)

## just for fun lets plot it to get a function idea

[plot](plot.py)

## thoughts

There must be a better solution and not this monster of complexity...
