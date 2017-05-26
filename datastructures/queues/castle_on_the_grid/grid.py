
from collections import defaultdict
from itertools import product
from queue import Queue

class Grid:
    """The playing grid.

    The data structure for the grid is a 2D list - this is as provided in the 
    question"""

    def __init__(self, data):

        self.data = data
        self.N = len(self.data)


    def is_valid(self, i, j):
        try:
            is_valid = self.data[i][j] and i >= 0 and j >= 0
        except IndexError:            
            is_valid = False

        return is_valid


class BuildGrid:

    obj = Grid

    @classmethod
    def from_hackerrank_input(cls, handler):
        
        data = []
        N = int(handler.readline().strip())
        for _ in range(N):
            data.append([])
            line = handler.readline().strip()
            for char in line:
                data[-1].append(char == '.')
        a_grid = cls.obj(data)

        a, b, c, d = map(int, handler.readline().strip().split())
        castle_coords = (a, b)
        target_coords = (c, d)

        return a_grid, castle_coords, target_coords


def play(game_grid, castle, target):

    # queue has coordinates and moves taken to get there

    min_moves_to_target = game_grid.N**2 + 1
    visited = defaultdict(lambda: game_grid.N**2 + 1)

    moves_queue = Queue()
    moves_queue.put((*castle, -1))

    while(not moves_queue.empty()):
        i, j, moves = moves_queue.get()
        moves += 1
        if game_grid.is_valid(i, j) and visited[i,j] > moves and moves < min_moves_to_target:
            visited[i,j] = moves
            if (i, j) == target:
                min_moves_to_target = min(min_moves_to_target, moves)
            else:
                for delta_i, delta_j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                    moves_queue.put((i + delta_i, j + delta_j, moves))

    return min_moves_to_target

