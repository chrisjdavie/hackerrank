
from functools import reduce
from operator import mul
from itertools import product, compress

class TooFewError(ValueError):
    pass


def all_two_factors(prime_factors):
    
    if len(prime_factors) < 2:
       raise TooFewError

    factors = set()
    
    for bools in product([True, False], repeat=len(prime_factors)):
        if all(bools) or not(any(bools)):
            continue

        f0 = list(compress(prime_factors,bools))
        f0 = reduce(mul, f0)

        not_bools = [ not x for x in bools ]
        f1 = list(compress(prime_factors,not_bools))
        f1 = reduce(mul, f1)
        factors.add((min(f0,f1),max(f0,f1)))

    return factors

