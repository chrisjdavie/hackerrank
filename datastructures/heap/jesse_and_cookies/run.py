
from heapq import heapify, heappush, heappop

_, minimum_sweetness = map(int,input().split())
cookies = list(map(int,input().split()))
heapify(cookies)

count = 0
while(cookies[0] < minimum_sweetness and len(cookies) > 1):
    count += 1
    new_cookie = heappop(cookies) + 2*heappop(cookies)
    heappush(cookies, new_cookie)

if cookies[0] < minimum_sweetness:
    count = -1

print(count)

