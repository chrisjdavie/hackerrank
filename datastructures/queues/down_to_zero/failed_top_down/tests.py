
import unittest

from functools import reduce
from operator import mul

from .all_two_factors import TooFewError, all_two_factors
from .game_stuff import next_numbers, play
from .primes import next_prime, prime_decomposition


class TestNextPrime(unittest.TestCase):

    def test_two(self):
        N = 2
        self.assertEqual(next_prime(N), N)


    def test_first_nontrivial_prime(self):
        N = 3
        self.assertEqual(next_prime(N), N)


    def test_odd_not_prime(self):
        self.assertEqual(next_prime(9),3)


class TestPrimeDecomposition(unittest.TestCase):

    def test_prime(self):
        
        N = 3
        primes = prime_decomposition(N)
        self.assertSequenceEqual(primes,[N])


    def test_duplicate_primes(self):

        primes_expected = [3]*2
        primes = prime_decomposition(reduce(mul,primes_expected))
        self.assertSequenceEqual(primes, primes_expected)


    def test_different_primes(self):

        primes_expected = [ 2, 3, 5 ]
        primes = prime_decomposition(reduce(mul,primes_expected))
        self.assertSequenceEqual(primes, primes_expected)


class TestAllTwoFactors(unittest.TestCase):

    def test_prime(self):

        p_factors = [ 2 ]

        self.assertRaises(TooFewError, all_two_factors, p_factors)

    def test_two_primes(self):

        p_factors = [ 2, 3 ]
        expected = set()
        expected.add(( 2, 3 ))

        self.assertEqual(all_two_factors(p_factors), expected)


    def test_three_identical_primes(self):

        p_factors = [ 2, 2, 2 ]
        expected = set()
        expected.add(( 2, 4 ))

        self.assertEqual(all_two_factors(p_factors), expected)


    def test_three_different_primes(self):

        p_factors = [ 2, 3, 4 ]
        expected = [( 4, 6 ),
                    ( 3, 8 ),
                    ( 2, 12)] 

        actual = all_two_factors(p_factors)
        for pair in expected:
            self.assertIn(pair, actual)


    def test_two_same_one_different_primes(self):

        p_factors = [ 2, 2, 3 ]
        expected = [( 2, 6 ),
                    ( 3, 4 )]

        actual = all_two_factors(p_factors)
        for pair in expected:
            self.assertIn(pair, actual)


class TestNextNumbers(unittest.TestCase):

    def test_prime(self):

        input_no = 17
        expected_output = [ 16 ]

        self.assertEqual(next_numbers(input_no), expected_output)


    def test_thirty(self):

        input_no = 30
        expected_output = [ 6, 10, 15, 29 ]

        self.assertEqual(sorted(next_numbers(input_no)),
                         expected_output)


class TestPlay(unittest.TestCase):

    def run_game(self, start_number, expected_moves):

        moves = play(start_number)

        self.assertEqual(expected_moves, moves)


    def test_one(self):

        self.run_game(1, 1)


    def test_two(self):

        self.run_game(2, 2)
    

    def test_three(self):

        self.run_game(3, 3)


    def test_15(self):

        self.run_game(15, 5)


    def test_thirty(self):

        self.run_game(30, 5)


    def test_large(self):
        
        self.run_game(966514, 8)


    def test_reg(self):

        self.run_game(577592, 8)


"""
Here, with my own caching, I got the sensible result for 1. I was also doing a 
very hacky check of what the cache was doing, but use pythons!

    def test_one(self):

        N = 1
        primes = prime_decomposition(N)
        self.assertSequenceEqual(primes,[])


    def test_caching(self):

        # populate cache by running (unittest clears globals, which is interesting)
        primes_expected = [ 2, 3, 5 ]
        prime_decomposition(reduce(mul,primes_expected))
        cache0 = prime_decomposition.__globals__['decomposition_cache']
        
        # check cache is populated
        for i in range(len(primes_expected)):
            cached_primes = primes_expected[i:]
            Q = reduce(mul,cached_primes)
            self.assertSequenceEqual(cache0[Q],
                                     cached_primes)

        prime_decomposition(reduce(mul,primes_expected))
        cache1 = prime_decomposition.__globals__['decomposition_cache']

        # checking cache is not repopulated
        self.assertEqual(cache0,cache1)
        self.assertIs(cache0[30],cache1[30])

"""

