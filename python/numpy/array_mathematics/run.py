
import numpy as np

N, M = map(int, input().split())

A_ij = np.zeros((N,M),int)
B_ij = np.zeros((N,M),int)

for i in range(N):
    A_ij[i] = np.array(input().split(), int)
for i in range(N):
    B_ij[i] = np.array(input().split(), int)

print(A_ij + B_ij)
print(A_ij - B_ij)
print(A_ij * B_ij)
print(A_ij// B_ij)
print(A_ij % B_ij)
print(A_ij** B_ij)


