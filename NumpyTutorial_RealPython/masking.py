import numpy as np

numbers = np.linspace(5,50,24).astype(int).reshape(4,-1)
print(numbers)

mask = numbers % 4 == 0
print(mask)
print(numbers[mask])

by_four = numbers[numbers % 4 == 0]
print(by_four)