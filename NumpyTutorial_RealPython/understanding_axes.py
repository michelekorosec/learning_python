import numpy as np

table = np.array([
   [5, 3, 7, 1],
   [2, 6, 7 ,9],
   [1, 1, 1, 1],
   [4, 3, 2, 0],
   ])

print(table.max())
print(table.max(axis=0))
print(table.max(axis=1))