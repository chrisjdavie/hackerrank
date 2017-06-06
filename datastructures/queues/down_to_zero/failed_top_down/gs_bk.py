
from queue import PriorityQueue

from .primes import prime_decomposition
from .all_two_factors import all_two_factors

def next_numbers(num):

    next_nums = []

    next_nums.append(num - 1)

    prime_factors = prime_decomposition(num)

    if len(prime_factors) > 1:
        for pair in all_two_factors(prime_factors):
            next_nums.append(max(pair))

    return next_nums


def play(num):

    all_numbers = PriorityQueue()

    # priority, (value, moves)
    all_numbers.put((num, 1))

    min_moves = num + 1

    while not all_numbers.empty():
        num, moves = all_numbers.get()

        if num == 1:
            min_moves = moves
        elif moves < min_moves:
            for next_num in next_numbers(num):
                all_numbers.put((next_num, moves + 1))

    return min_moves

