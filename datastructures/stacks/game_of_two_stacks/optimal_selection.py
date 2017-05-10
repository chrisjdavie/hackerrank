import copy

from itertools import accumulate

def max_score(A, B, x):

    # making everything zero indexed

    A = copy.copy(A)
    A.insert(0,0)
    A_accu = list(accumulate(A))
    B_accu_rev = list(accumulate(B))[::-1]

    max_score = 0

    A_i = A_accu.pop()
    i = len(A_accu)

    B_j = 0
    j = 0

    while(A_accu and B_accu_rev):
        if A_i + B_j <= x:
            # less than answer, increase
            max_score = max((max_score, i + j))
            B_j = B_accu_rev.pop()
            j += 1
        else:
            # more than answer, decrease
            A_i = A_accu.pop()
            i = len(A_accu)

    else:
        if (A_i + B_j <= x):
            max_score = max((max_score, i + j))  


    while(B_accu_rev):
        B_j = B_accu_rev.pop()
        j += 1
        if A_i + B_j <= x:
            max_score = max((max_score, i + j))
        else:
            break


    while(A_accu):
        A_i = A_accu.pop()
        i = len(A_accu)
        if A_i + B_j <= x:
            max_score = max((max_score, i + j))
            break


    return max_score

