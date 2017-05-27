
from io import StringIO
import unittest

from .grid import Grid, BuildGrid, play

class TestGrid(unittest.TestCase):

    
    def build_grid(self, N):
        data = []
        for _ in range(N):
            data.append([ True ]*N)
        return data


    def test_init(self):

        N = 6
        
        data = self.build_grid(N)
        a_grid = Grid(data)

        self.assertSequenceEqual(a_grid.data, data)
        self.assertEqual(a_grid.N, N)


    def test_is_valid(self):

        N = 3
        
        data = self.build_grid(N)
        a_grid = Grid(data)

        self.assertIs(a_grid.is_valid(1,2),True)


    def test_is_not_valid_lower_bounds(self):

        data = self.build_grid(3)
        a_grid = Grid(data)

        self.assertIs(a_grid.is_valid(-1, 1), False)
        self.assertIs(a_grid.is_valid(1, -2), False)


    def test_is_not_valid_upper_bounds(self):

        N = 3

        data = self.build_grid(N)
        a_grid = Grid(data)

        self.assertIs(a_grid.is_valid(N, 1), False)
        self.assertIs(a_grid.is_valid(1, N+1), False)


    def test_is_not_valid_forbidden(self):

        data = self.build_grid(3)
        j, i = 1, 2
        data[j][i] = False

        a_grid = Grid(data)

        self.assertIs(a_grid.is_valid(j, i), False)


class TestBuildGrid(unittest.TestCase):


    def test_from_hackerrank_input(self):

        sample_input = ( "3\n"
                         ".X.\n"
                         ".X.\n"
                         "...\n"
                         "0 0 0 2" )
        sh = StringIO(sample_input)

        N = 3
        expected_grid = [ [ True, False, True ],
                          [ True, False, True ],
                          [ True, True,  True ] ]
        coords_castle_expected = (0, 0)
        coords_target_expected = (0, 2)

        grid_out, coords_castle_out, coords_target_out = BuildGrid.from_hackerrank_input(sh)

        self.assertSequenceEqual(grid_out.data, expected_grid)
        self.assertEqual(grid_out.N, N)
        self.assertSequenceEqual(coords_castle_out, coords_castle_expected)
        self.assertSequenceEqual(coords_target_out, coords_target_expected)


class TestPlay(unittest.TestCase):

    def test_no_moves(self):

        
        data = [[True]]
        a_grid = Grid(data)

        castle = (0, 0)
        target = (0, 0)

        self.assertEqual(play(a_grid, castle, target), 0)

    
    def test_move_left(self):
        
        data = [ [True, True],
                 [True, True] ]
        a_grid = Grid(data)
        castle = (0, 1)
        target = (0, 0)

        self.assertEqual(play(a_grid, castle, target), 1)


    def test_move_up(self):

        data = [ [True, True],
                 [True, True] ]
        a_grid = Grid(data)
        castle = (1, 0)       
        target = (0, 0)

        self.assertEqual(play(a_grid, castle, target), 1)


    def test_move_up_left(self):

        data = [ [True, True],
                 [True, True] ]
        a_grid = Grid(data)
        castle = (1, 1)
        target = (0, 0)
        self.assertEqual(play(a_grid, castle, target), 2)


    def test_solution_with_forbidden(self):

        data = [ [True, False, True],
                 [True, True,  True],
                 [True, True,  True] ]
        a_grid = Grid(data)
        castle = (0, 2)
        target = (0, 0)
        self.assertEqual(play(a_grid, castle, target), 3)


    def test_two_valid_solutions_different_lengths(self):

        data = [ [True, True,  True, True],
                 [True, False, True, True],
                 [True, False, True, True],
                 [True, True,  True, True] ]
        a_grid = Grid(data)
        castle = (1, 0)
        target = (1, 2)
        self.assertEqual(play(a_grid, castle, target), 3)


class TestRegression(unittest.TestCase):

    def test_from_hackerrank_0(self):
        # This came from not including the direction in the dictionary that was caching the
        # the moves taken to get to a square

        data = [ [True, True, True,  True],
                 [True, True, True,  True],
                 [True, True, True,  True],
                 [True, True, False, True] ]
        a_grid = Grid(data)
        castle = (3, 0)
        target = (3, 3)
        self.assertEqual(play(a_grid, castle, target), 3)

