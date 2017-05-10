
import unittest

from .optimal_selection import max_score

class TestSelect(unittest.TestCase):

    def test_singular(self):

        A = [ 1 ]
        B = [ 1 ]
        x = 1
        score = max_score(A, B, x)
        self.assertEqual(score, 1)


    def test_more_than_one_solution_pick_optimal(self):

        A = [ 1, 2, 2, 2 ]
        B = [ 1, 1, 2, 2, 2 ]
        x = 5
        score = max_score(A, B, x)
        self.assertEqual(score, 4)
        score = max_score(B, A, x)
        self.assertEqual(score, 4)


    def test_only_A_only_B(self):

        A = [ 1, 1, 1, 2 ]
        B = [ 2, 1, 1, 2 ]
        x = 3
        score = max_score(A, B, x)
        self.assertEqual(score, 3)
        
        score = max_score(B, A, x)
        self.assertEqual(score, 3)


    def test_zeros(self):

        A = [ 0 ]
        B = [ 1 ]
        x = 1
        score = max_score(A, B, x)
        self.assertEqual(score, 2)
        score = max_score(B, A, x)
        self.assertEqual(score, 2)



