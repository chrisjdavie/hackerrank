
import unittest

from functools import reduce
from operator import mul

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

