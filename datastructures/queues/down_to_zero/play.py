
from math import sqrt

def play(initial_val):
    
    if initial_val < 1:
        return initial_val

    vals_to_process = []
    vals_to_process.append((initial_val, 1))
    visited = [ 0 ] * initial_val

    while vals_to_process:

        val, moves = vals_to_process.pop(0)
        if val == 1:
            return moves

        i = int(sqrt( val ))
        while i > 1:
            if not val%i:
                new_val = val//i
                if not visited[new_val]:
                    vals_to_process.append((new_val, moves+1))
                    visited[new_val] = 1
            i -= 1

        if not visited[val-1]:
            vals_to_process.append((val-1, moves+1))
            visited[val-1] = 1
