
from functools import lru_cache, partial
from queue import Queue

from .primes import prime_decomposition
from .all_two_factors import all_two_factors


@lru_cache(None)
def next_numbers(num):

    next_nums = []

    next_nums.append(num - 1)

    prime_factors = prime_decomposition(num)

    if len(prime_factors) > 1:
        for pair in all_two_factors(prime_factors):
            next_nums.append(max(pair))

    return next_nums


def play(initial_num):
    
    all_numbers = Queue()

    already_visited = set()

    # value, moves to get here
    all_numbers.put((initial_num, [initial_num], 1))
    already_visited.add(initial_num)    

    while not all_numbers.empty():
        num, previous_vals, moves = all_numbers.get()
        if num == 1:
            print(previous_vals)
            break

        nns = next_numbers(num)

        for next_num in nns:
            if next_num not in already_visited:
                already_visited.add(next_num)
                all_numbers.put((next_num, previous_vals + [next_num], moves+1))

    return moves

