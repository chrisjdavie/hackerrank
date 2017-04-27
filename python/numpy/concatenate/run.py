
import numpy as np

N, M, P = map(int, input().split())

array_0 = np.zeros((N, P), int)
array_1 = np.zeros((M, P), int)

for i in range(N):
    array_0[i] = np.array(input().split(), int)
for i in range(M):
    array_1[i] = np.array(input().split(), int)

print(np.concatenate((array_0, array_1)))


