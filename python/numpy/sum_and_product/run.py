
import numpy as np

I, J = map(int, input().split())

array = np.zeros((I, J))

for i in range(I):
    array[i] = np.array(input().split())

arr_sum = np.sum(array, axis=0)
print(int(np.prod(arr_sum)))

