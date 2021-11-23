import numpy as np

square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
])

#print(square)
#print(np.shape(square))

for i in range(4):
    assert square[:,i].sum() == 34
    assert square[i,:].sum() == 34

assert square[:2,:2].sum() == 34

assert square[2:,:2].sum() == 34

assert square[:2,2:].sum() == 34

assert square[2:,2:].sum() == 34