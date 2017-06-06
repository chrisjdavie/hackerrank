
from queue import Queue

def play(initial_val):
    
    if initial_val < 1:
        return initial_val

    vals_to_process = Queue()
    vals_to_process.put((initial_val, 1))

    while not vals_to_process.empty():

        val, moves = vals_to_process.get()
        if val == 1:
            return moves

        vals_to_process.put((val-1, moves+1))
        for i in range(2, int(val**0.5) + 1):
            if not val%i:
                vals_to_process.put((val//i, moves+1))
    
