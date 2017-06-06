
from unittest import TestCase

from .play import play

class TestSetupmoves(TestCase):

    def test_one(self):

        input_val = 1
        moves = play(input_val)

        self.assertEqual(moves, 1)


    def test_two(self):

        input_val = 2
        moves = play(input_val)

        self.assertEqual(moves, 2)


    def test_three(self):

        input_val = 3
        moves = play(input_val)

        self.assertEqual(moves, 3)


    def test_4(self):

        input_val = 4
        moves = play(input_val)

        self.assertEqual(moves, 3)

    def test_15(self):

        input_val = 15
        moves = play(input_val)

        self.assertEqual(moves, 5)


    def test_30(self):

        input_val = 30
        moves = play(input_val)

        self.assertEqual(moves, 5)     


    def test_36(self):

        input_val = 36
        moves = play(input_val)

        self.assertEqual(moves, 5)   


    def test_reg_0(self):
         
        input_val = 393991
        moves = play(input_val)
   
        self.assertEqual(moves, 8)


    def test_reg_1(self):
        
        input_val = 966514
        moves = play(input_val)

        self.assertEqual(moves, 8) 


    def test_reg_2(self):
        
        input_val = 0
        moves = play(input_val)

        self.assertEqual(moves, 0) 



