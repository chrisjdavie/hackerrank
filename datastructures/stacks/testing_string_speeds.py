
import random

N = 1000000000
b = [ 'a' ]*N

for i in range(N):
    b[i] = chr(65 + random.randint(0,26))


def test():
    global b

    def using_pop(b, k):
        for _ in range(k):
            b.pop()
        return b


    def using_list_cmp(b, k):
        return b[:-k]

    b = using_pop(b, 3)

import timeit
print(timeit.timeit("test()", number=10, setup="from __main__ import test"))
