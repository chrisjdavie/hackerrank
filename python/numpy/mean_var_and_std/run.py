
import numpy as np

N, M = map(int, input().split())

array = np.zeros((N, M), int)

for i in range(N):
    array[i] = np.array(input().split(), int)

print(np.mean(array, axis = 1))
print(np.var(array, axis = 0))
print(np.std(array))


