from typing import Tuple, List, Optional

# some helper
getter = lambda m,p : m[p[0]][p[1]]

get_neighbours = lambda p: [ (p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1) ]
    
def setter(m, p, v):
    m[p[0]][p[1]] = v

def calc_smallest_step_number(board :List[List[bool]], start :Tuple[int,int], end :Tuple[int,int]) -> Optional[int]:
    # Helper and Preconditions
    N,M = len(board), len(board[0])
    is_stepable= lambda p : 0 <= p[0] < N and 0 <= p[1] < M and not getter(board, p)
    assert is_stepable(start)
    assert is_stepable(end)

    distances = [ [None]*M for _ in range(N)]
    distances[end[0]][end[1]] = 0
    nexts = list()
    for neighbour in get_neighbours(end):
        if is_stepable(neighbour):
            nexts.append(neighbour)
    while len(nexts) > 0:
        point = nexts.pop()
        min_distance = N*M
        for neighbour in get_neighbours(point):
            if is_stepable(neighbour):
                distance = getter(distances, neighbour)
                if distance != None:
                    min_distance = min(min_distance, distance + 1)
                else:
                    nexts.append(neighbour)
        distances[point[0]][point[1]] = min_distance
        if point == start:  break

    # for distance in distances: print(distance)
    return getter(distances, start)


import unittest

class TestCalcSmallestStepNumber(unittest.TestCase):

    def parse_board(self, board: str) -> List[List[int]]:
        board = board.strip()
        board = list(filter(lambda x : x in "ft\n", board.strip()))
        matrix = list()
        matrix.append(list())
        row = 0
        for item in board:
            if item == "\n":
                matrix.append(list())
                row += 1
            elif item == "t":
                matrix[row].append(True)
            elif item == "f":
                matrix[row].append(False)
        # check, if the board is a clumsy missformed matrix
        for row in matrix[1:]:
            assert len(matrix[0]) == len(row)
        return matrix

    def test_unreachable(self):
        board_str = """
        fffff
        ftfft
        tfttf
        fffff
        """
        """
         0 1 2 3 4
         1 . 3 4 .
         . - . . -
         - - - - -
        """

        board = self.parse_board(board_str)
        self.assertEqual(calc_smallest_step_number(board, (3,0), (0,0)), None)

    def test_example(self):
        board_str = """
        [[f, f, f, f],
         [t, t, f, t],
         [f, f, f, f],
         [f, f, f, f]]
        """
        """
         0 1 2 3
         . . 3 .
         6 5 4 5
         7 6 5 6
        """
        board = self.parse_board(board_str)
        self.assertEqual(calc_smallest_step_number(board, (3,0), (0,0)), 7)
        self.assertEqual(calc_smallest_step_number(board, (0,0), (3,0)), 7)

    def test_long(self):
        board_str = """
        ftffftfff
        ffftffftf
        ttttttttf
        ffftffftf
        ftffftfff
        ftttttttt
        ftffftfff
        ffftffftt
        """
        """
         0  .  4  5  6  . 10 11 12
         1  2  3  .  7  8  9  . 13
         .  .  .  .  .  .  .  . 14
        27 26 25  . 21 20 19  . 15
        28  . 24 23 22  . 18 17 16
        29  .  .  .  .  .  .  .  .
        30  . 34 35 36  . 40 41 42
        31 32 33  . 37 38 39  .  .
        ..........................
        """
        board = self.parse_board(board_str)
        self.assertEqual(calc_smallest_step_number(board, (6,8), (0,0)), 42)


if __name__ == "__main__":
    unittest.main()
