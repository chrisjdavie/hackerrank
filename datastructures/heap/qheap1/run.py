
from heapq import heappush, heappop

heap = []
del_heap = []

Q = int(input())

for _ in range(Q):
    query = input()
    if query[0] == '1':
        val = int(query.split()[1])
        heappush(heap, val)
    if query[0] == '2':
        val = int(query.split()[1])
        heappush(del_heap, val)
        while del_heap and del_heap[0] == heap[0]:
            heappop(heap)
            heappop(del_heap)
    if query[0] == '3':
        print(heap[0])

