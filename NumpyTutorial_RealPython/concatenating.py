import numpy as np

a = np.array([
    [4,8],
    [6,1],
])

b = np.array([
    [3,5],
    [7,2],
])

print(np.hstack((a,b)))
print(np.vstack((b,a)))
print(np.concatenate((a,b)))
print(np.concatenate((a,b),axis=None))
