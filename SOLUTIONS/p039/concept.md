# game of life simulation

This cellular automata is a well known simulation.

The requirment, that the world is infinite is a problem for this, but there are some solutions. So we have to go away from a static grid, and use something similar to get all living cells and its neighbours. A hash set or map (coord -> cell) is a good alternative.

## Data structures

```pseudo
struct coord:
  x :int
  y :int
  hash() :int
  neighbours() :[coord]


struct world:
  alive: set[coord]
  ul,br : coord for bounderies
  init(alive)
  iterate()
  display()
```

## Algo

```pseudo
gol_simulate(step, init_living :{Coord}):
  world.init(init_alive)
  world.display()
  do step times:
    world.iterate()
    world.display()
```

### more in detail

```pseudo

world::init(init_alive: set):
  alive = init_alive
  _get_world_bounderies() -> lu = ( min(x in alvie), min(y in alvie), br = (max(x in alvie), max(y in alvie)

world::display():
  print(step)
  for y in lu.y ... br.y +1:
    print(newline)
    for x in lu.x ... br.x +1:
       if (x,y) in alive:
         print("*")
       else:
         print(".")

world::iterate()
  to_check = for each cell in alive, get all neighbour cell set
  new_alive = set()
  for each cell in to_check:
    if check in alive:
      if 2 or 3 neighbours are in alive: new_alive.add(cell)
    else:
      if 3 neighbours are in alive: new_alive.add(cell)
  alive = new_alive
  _get_world_bounderies()
```

[code](solution.py)
