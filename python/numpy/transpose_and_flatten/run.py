import numpy as np

N, M = map(int, input().split())
array = np.zeros((N, M), int)

for i in range(N):
    array[i] = np.array(input().split(), int)

print(np.transpose(array))
print(array.flatten())

