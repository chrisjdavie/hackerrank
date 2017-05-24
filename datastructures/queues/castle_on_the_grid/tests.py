
import unittest

from .grid import Grid, play

class TestGrid(unittest.TestCase):

    def test_init(self):

        N = 6

        a_grid = Grid(N)

        self.assertEqual(a_grid.N, N)
        self.assertEqual(len(a_grid.forbidden), 0)
        self.assertEqual(len(a_grid.castle), 0)


    def test_add_forbidden(self):

        a_grid = Grid(3)

        i, j = 1, 2

        a_grid.add_forbidden(i, j)

        self.assertIn((i,j), a_grid.forbidden)


    def test_is_valid(self):

        a_grid = Grid(3)

        self.assertIs(a_grid.is_valid(1,2),True)


    def test_is_not_valid_lower_bounds(self):

        a_grid = Grid(3)

        self.assertIs(a_grid.is_valid(-1, 1), False)
        self.assertIs(a_grid.is_valid(1, -2), False)


    def test_is_not_valid_upper_bounds(self):

        N = 3

        a_grid = Grid(N)

        self.assertIs(a_grid.is_valid(N, 1), False)
        self.assertIs(a_grid.is_valid(1, N+1), False)


    def test_is_not_valid_forbidden(self):

        a_grid = Grid(3)

        i, j = 1, 2

        a_grid.add_forbidden(i, j)

        self.assertIs(a_grid.is_valid(i, j), False)


    def test_set_castle(self):

        a_grid = Grid(3)

        i, j = 1, 2

        a_grid.set_castle(i, j)

        self.assertSequenceEqual((i, j), a_grid.castle)


    def test_is_castle(self):

        a_grid = Grid(3)

        i, j = 1, 2

        a_grid.set_castle(i, j)

        self.assertIs(a_grid.is_castle(i+1, j), False)
        self.assertIs(a_grid.is_castle(i, j), True)
    

class TestPlay(unittest.TestCase):

    def test_no_moves(self):

        N = 1
        forbidden = []
        castle = (0, 0)
        start = (0, 0)

        self.assertEqual(play(N, forbidden, castle, start), 0)

    
    def test_move_left(self):

        N = 2
        forbidden = []
        start = (0, 0)
        castle = (1, 0)

        self.assertEqual(play(N, forbidden, castle, start), 1)


    def test_move_up(self):

        N = 2
        forbidden = []
        start = (0, 0)
        castle = (0, 1)

        self.assertEqual(play(N, forbidden, castle, start), 1)


    def test_move_up_left(self):

        N = 2
        forbidden = []
        start = (0, 0)
        castle = (1, 1)
        self.assertEqual(play(N, forbidden, castle, start), 2)


    def test_longer_solution_with_forbidden(self):

        N = 3
        forbidden = [ (1,0) ]
        start = (0, 0)
        castle = (0, 2)
        self.assertEqual(play(N, forbidden, castle, start), 4)


    def test_two_valid_solutions_different_lengths(self):

        N = 4
        forbidden = [ (1, 1), (1, 2) ]
        start = (0, 1)
        castle = (2, 1)
        self.assertEqual(play(N, forbidden, castle, start), 4)

