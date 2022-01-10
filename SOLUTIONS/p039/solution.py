"""Test
    >>> blinker = {Coord(x, y) for x, y in [(-1, 0), (0, 0), (1, 0)]}
    >>> gol_simulate(4, blinker)
    step:  0 --- x:[-1,1], y:[0,0]
    * * *
    <BLANKLINE>
    step:  1 --- x:[0,0], y:[-1,1]
    *
    *
    *
    <BLANKLINE>
    step:  2 --- x:[-1,1], y:[0,0]
    * * *
    <BLANKLINE>
    step:  3 --- x:[0,0], y:[-1,1]
    *
    *
    *
    <BLANKLINE>
    step:  4 --- x:[-1,1], y:[0,0]
    * * *
    
    >>> gol_simulate(1, {Coord(0, 0)})
    step:  0 --- x:[0,0], y:[0,0]
    *
    <BLANKLINE>
    step:  1 --- ALL DEAD
    
    >>> glider = {Coord(x, y) for x, y in [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]}
    >>> gol_simulate(4, glider)
    step:  0 --- x:[0,2], y:[0,2]
    . * .
    . . *
    * * *
    <BLANKLINE>
    step:  1 --- x:[0,2], y:[1,3]
    * . *
    . * *
    . * .
    <BLANKLINE>
    step:  2 --- x:[0,2], y:[1,3]
    . . *
    * . *
    . * *
    <BLANKLINE>
    step:  3 --- x:[1,3], y:[1,3]
    * . .
    . * *
    * * .
    <BLANKLINE>
    step:  4 --- x:[1,3], y:[1,3]
    . * .
    . . *
    * * *
"""

from typing import Set


class Coord(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return f'(x:{self.x},y:{self.y})'

    def neigbours(self):
        return [Coord(self.x+i, self.y+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]


class World(object):
    def __init__(self, alive):
        self.alive = alive
        self.step = 0
        self._set_world_bounderies()

    def _set_world_bounderies(self):
        minx, miny, maxx, maxy = float('inf'), float(
            'inf'), -float('inf'), -float('inf')
        for cell in self.alive:
            minx = min(minx, cell.x)
            miny = min(miny, cell.y)
            maxx = max(maxx, cell.x)
            maxy = max(maxy, cell.y)
        self.ul = Coord(minx, miny)
        self.br = Coord(maxx, maxy)

    def iterate(self):
        # to_check = {cell.neigbours() for cell in self.alive}
        to_check = set()
        to_check.update(self.alive)
        for cell in self.alive:
            to_check.update(cell.neigbours())

        new_alive = set()
        for cell in to_check:
            live_neigbours = sum(n in self.alive for n in cell.neigbours())
            if (
                (cell in self.alive
                 and live_neigbours in [2, 3])
                or (cell not in self.alive
                    and live_neigbours == 3)
            ):
                new_alive.add(cell)
        self.alive = new_alive
        self._set_world_bounderies()
        self.step += 1

    def display(self):
        if not self.alive:
            print(f'step:{self.step:3d} --- ALL DEAD')
            return
        print(
            f'step:{self.step:3d} --- x:[{self.ul.x},{self.br.x}], y:[{self.ul.y},{self.br.y}]')
        for y in range(self.ul.y, self.br.y + 1):
            row = []
            for x in range(self.ul.x, self.br.x + 1):
                row += ["*"] if Coord(x, y) in self.alive else ["."]
            print(" ".join(row))


def gol_simulate(steps: int, alive: Set[Coord]) -> None:
    world = World(alive)
    world.display()
    for _ in range(steps):
        print()  # en extra line
        world.iterate()
        world.display()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Fome funny simulation
    block0 = {Coord(x, y)
              for x, y in [(-10, -10), (-9, -10), (-10, -9), (-9, -9)]}
    block1 = {Coord(x, y) for x, y in [(10, -10), (9, -10), (10, -9), (9, -9)]}
    block2 = {Coord(x, y) for x, y in [(-10, 10), (-9, 10), (-10, 9), (-9, 9)]}
    block3 = {Coord(x, y) for x, y in [(10, 10), (9, 10), (10, 9), (9, 9)]}

    glider = {Coord(x, y) for x, y in [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]}
    blinker = {Coord(x, y) for x, y in [(-1, 0), (0, 0), (1, 0)]}

    init_set = set()
    init_set.update(block0)
    init_set.update(block1)
    init_set.update(block2)
    init_set.update(block3)
    init_set.update(glider)
    gol_simulate(10, init_set)
