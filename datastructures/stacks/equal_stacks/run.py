
from .common_height import highest_common

input()
n0 = list(map(int, input().split()))[::-1]
n1 = list(map(int, input().split()))[::-1]
n2 = list(map(int, input().split()))[::-1]

print(highest_common([ n0, n1, n2 ]))
