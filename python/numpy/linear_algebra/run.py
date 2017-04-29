
import numpy as np

I = int(input())

A_ij = np.zeros((I,I), float)

for i in range(I):
    A_ij[i] = np.array(input().split(), float)

print(np.linalg.det(A_ij))

