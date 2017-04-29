
import numpy as np

A_i = np.array(input().split(), int)
B_i = np.array(input().split(), int)

print(np.inner(A_i,B_i))
print(np.outer(A_i,B_i))

