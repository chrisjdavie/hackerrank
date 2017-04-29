
import numpy as np

I, J = map(int, input().split())

array = np.zeros((I,J),int)

for i in range(I):
    array[i] = np.array(input().split(),int)

min_arr = np.min(array, axis=1)
print(np.max(min_arr))

