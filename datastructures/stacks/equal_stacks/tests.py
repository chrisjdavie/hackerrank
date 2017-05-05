
import unittest

from .common_height import highest_common


class TestHighest(unittest.TestCase):

    def test_same_height(self):

        n1 = [ 1 ]
        n2 = [ 1 ]
        n3 = [ 1 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 1)


    def test_one_higher(self):

        n1 = [ 1, 1 ]
        n2 = [ 1 ]
        n3 = [ 1 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 1)


    def test_two_higher(self):

        n1 = [ 1, 1 ]
        n2 = [ 1, 1 ]
        n3 = [ 1 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 1)


    def test_all_higher(self):

        n1 = [ 1, 1 ]
        n2 = [ 1, 1 ]
        n3 = [ 1, 2 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 1)


    def test_no_common_height(self):

        n1 = [ 1 ]
        n2 = [ 1 ]
        n3 = [ 2 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 0)


    def test_different_stacked_base(self):

        n1 = [ 1, 2 ]
        n2 = [ 2, 1 ]
        n3 = [ 1, 1, 1 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 3)


    def test_hackerrank(self):

        n1 = [ 1, 1, 1, 2, 3 ]
        n2 = [ 2, 3, 4 ]
        n3 = [ 1, 4, 1, 1 ]

        height = highest_common([n1, n2, n3])

        self.assertEqual(height, 5)

