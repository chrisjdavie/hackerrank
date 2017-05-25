
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
        i, j = 1, 2
        data[i][j] = False

        a_grid = Grid(data)

        self.assertIs(a_grid.is_valid(i, j), False)


class TestBuildGrid(unittest.TestCase):

    def mock_handler(self, N, string_grid, coords_castle, coords_target):
        """mocking the stdin of hackerrank"""
        
        yield str(N)
        for line in string_grid:
            yield line
        yield "{} {} {} {}".format(*coords_castle, *coords_target)


    def test_from_hackerrank_input(self):

        N = 3
        string_grid = [ ".X.",
                        ".X.",
                        "..." ]
        expected_grid = [ [ True, False, True ],
                          [ True, False, True ],
                          [ True, True,  True ] ]
        coords_castle_expected = (0, 0)
        coords_target_expected = (0, 2)

        class MockHandler:
            def __init__(self, mh):
                self.mh = mh
    
            def read(self):
                return self.mh.__next__()

        mh = self.mock_handler(N, string_grid, coords_castle_expected, coords_target_expected)
        mh = MockHandler(mh)

        grid_out, coords_castle_out, coords_target_out = BuildGrid.from_hackerrank_input(mh)

        self.assertSequenceEqual(grid_out.data, expected_grid)
        self.assertEqual(grid_out.N, N)
        self.assertSequenceEqual(coords_castle_out, coords_castle_expected)
        self.assertSequenceEqual(coords_target_out, coords_target_expected)


"""
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
"""
