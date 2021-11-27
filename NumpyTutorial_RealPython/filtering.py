import numpy as np
from numpy.random import default_rng

rng = default_rng()

values = rng.standard_normal(10000)
print(values[:5])

std = values.std()
print(std)

filtered = values[(values > -2 * std)&(values < 2 * std)]
print(filtered.size)

print(filtered.size/values.size)