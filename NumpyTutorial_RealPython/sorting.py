import numpy as np

data = np.array([
    [7,1,4],
    [8,6,5],
    [1,2,3],
])

print(np.sort(data))
print(np.sort(data,axis=None))
print(np.sort(data,axis=0))