
from functools import lru_cache

from .interesting_maths.sieve_of_eratosthenes import generate_primes, generator_cached

gen_primes = generator_cached(generate_primes, N = 10**6)


@lru_cache(maxsize=None)
def next_prime(Q):
    for prime in gen_primes():
        if not Q%prime:
            return prime


@lru_cache(maxsize=None)
def prime_decomposition(Q):
    np = next_prime(Q)
    next_Q = Q // np

    primes = [np]
    if next_Q > 1:
        primes += prime_decomposition(next_Q)
    
    return primes

"""
Did this directly, and then realised if I did it
recursively, I'd be able to use lru_cache and 
discard my own stuff.

decomposition_cache = {}
def prime_decomposition(Q_orig):

    Qs_visited = []
    primes = []
    Q = Q_orig
    while Q > 1:
        if Q in decomposition_cache:
            decomp_primes = decomposition_cache[Q]
            break
        Qs_visited.append(Q)
        np = next_prime(Q)
        primes.append(np)
        Q //= np
    else:
        decomp_primes = []

    primes += decomp_primes
    for i, Q_int in enumerate(Qs_visited):    
        decomposition_cache[Q_int] = primes[i:]

    return primes
"""
