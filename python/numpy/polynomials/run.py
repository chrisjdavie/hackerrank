
import numpy as np

P = np.array(input().split(), float)
x = float(input())

print(np.polyval(P, x))



