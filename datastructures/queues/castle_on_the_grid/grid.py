
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


    def is_valid(self, j, i):
        try:
            is_valid = self.data[j][i] and i >= 0 and j >= 0
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

    # queue has coordinates, moves and preceeding direction taken to get there

    min_moves_to_target = game_grid.N**2 + 1
    visited = defaultdict(lambda: game_grid.N**2 + 1)

    seach_queue = Queue()
    seach_queue.put((*castle, 0, None))

    while(not seach_queue.empty()):
        j, i, moves, dirn_old = seach_queue.get()

        if (j, i) == target:
            min_moves_to_target = min(min_moves_to_target, moves)

        elif game_grid.is_valid(j, i) and visited[j, i, dirn_old] > moves and moves < min_moves_to_target:
            visited[j, i, dirn_old] = moves

            for dirn_new in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                moves_new = moves + (dirn_new != dirn_old)
                seach_queue.put((j + dirn_new[0], i + dirn_new[1], moves_new, dirn_new))

    return min_moves_to_target

