
from unittest import TestCase

from .play import setup_struct

class TestSetupStruct(TestCase):

    def test_one(self):

        target_vals = {1}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[1], 1)


    def test_two(self):

        target_vals = {2}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[2], 2)


    def test_three(self):

        target_vals = {3}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[3], 3)


    def test_4(self):

        target_vals = {4}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[4], 3)

    def test_15(self):

        target_vals = {15}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[15], 5)


    def test_30(self):

        target_vals = {30}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[30], 5)     


    def test_36(self):

        target_vals = {43}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[36], 5)   


    def test_reg_0(self):
         
        target_vals = {393991}
        struct = setup_struct(target_vals)
   
        self.assertEqual(struct[393991], 8)


    def test_reg_1(self):
        
        target_vals = {966514}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[966514], 8) 


    def test_reg_2(self):
        
        target_vals = {3}
        struct = setup_struct(target_vals)

        self.assertEqual(struct[0], 0) 



