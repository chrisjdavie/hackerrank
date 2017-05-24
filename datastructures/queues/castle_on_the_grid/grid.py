

class Grid:

    def __init__(self, N):

        self.N = N
        self.forbidden = set()
        self.castle = ()

    
    def add_forbidden(self, i, j):
        self.forbidden.add((i, j))


    def is_valid(self, i, j):

        is_valid = (i >= 0) and (j >= 0) and (i < self.N) and (j < self.N) \
            and (i, j) not in self.forbidden

        return is_valid


    def set_castle(self, i, j):

        self.castle = (i, j)


    def is_castle(self, i, j):

        return self.castle == (i, j)


def play(N, forbidden, castle, start):
    pass
