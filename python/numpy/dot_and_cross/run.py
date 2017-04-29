
import numpy as np

N = int(input())

A_ij = np.zeros((N,N),int)
B_ij = np.zeros((N,N),int)

for i in range(N):
    A_ij[i] = np.array(input().split(), int)
for i in range(N):
    B_ij[i] = np.array(input().split(), int)

AB_ij = np.dot(A_ij, B_ij)

print(AB_ij)

