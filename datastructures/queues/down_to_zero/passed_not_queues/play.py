
from copy import copy

def setup_struct(values_missing):

    targ_max = max(values_missing)
    next_val = [ targ_max + 2 ]*(targ_max + 2)
    
    next_val[0] = 0
    next_val[1] = 1
    next_val[2] = 2

    for i in range(2, targ_max):
        moves = next_val[i] + 1
        if next_val[i + 1] > moves:
            next_val[i + 1] = moves
        for j in range(2, min(i + 1, targ_max//i + 1)):
            if next_val[j*i] > moves:
                next_val[j*i] = moves
    
    return next_val


