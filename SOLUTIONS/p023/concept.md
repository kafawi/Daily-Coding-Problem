# Something like Dijkstra

We are searching for the fastes path for the givien matrix, that represents a map with tiles that are either walls or free to move on.

For every step it has a weigth of 1 (from free tile to another) or a infinitiy.
We can symoblizie the infinity with `null`.

So the algorithm goes like this (we start at the `end` but a start at `start` is here the same):

1. Build a matrix for the distance of the shape of the input, initialiize it with `null` for every entry.
2. create a queue to hold the next fields to keep track
3. setting distance matrix at point `end` to `0`
4. for all `end`s neighbours that are in the grid and in the input not `true` (Wall): put them into the queue
5. while queue is not empty:
    1. point = queue.pop()
    2. distance matrix at that point  = get minimum of all it's neighbours that are not `null` + 1
    3. for all points neighbours that are still `null` and in the input not `true` (Wall): put them into the queue
6. return value in the distance matrix at `start`

## signatur and other stuff

```pseudo_ocl
calc_smalles_step_number(board :matrix<bool>, start :point(x: int, y: int), end :(x: int, y: int)) -> {int, null}:
precondition: 
  0 <= start.x < matrix.shape.x
  0 <= end.x < matrix.shape.x
  0 <= start.y < matrix.shape.y
  0 <= end.y < matrix.shape.y
  board[start] == False
  board[end] == False

postcondition:
  if start there is no path from start to end
    return null
  else:
    return minimal number of steps from start to end
```

## a little tweek

we can break the loop, if we reach the `start` point.

[code](solution.py)
