
from collections import deque

from math import sqrt

def play(initial_val):
    
    if initial_val < 1:
        return initial_val

    vals_to_process = deque()
    vals_to_process.append((initial_val, 1))
    visited = set()

    while vals_to_process:

        val, moves = vals_to_process.popleft()
        if val == 1:
            return moves

        for i in range(2, int(sqrt( val )) + 1):
            if not val%i:
                new_val = val//i
                if new_val not in visited:
                    vals_to_process.append((new_val, moves+1))
                    visited.add(new_val)

        if val-1 not in visited:
            vals_to_process.append((val-1, moves+1))
            visited.add(val-1)
