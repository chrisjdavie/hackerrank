

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
        N = int(handler.read())
        for _ in range(N):
            data.append([])
            line = handler.read()
            for char in line:
                data[-1].append(char == '.')
        a_grid = cls.obj(data)

        a, b, c, d = map(int, handler.read().split())
        castle_coords = (a, b)
        target_coords = (c, d)

        return a_grid, castle_coords, target_coords


def play(N, forbidden, castle, start):
    pass
