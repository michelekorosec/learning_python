import numpy as np
import matplotlib.pyplot as plt

x = np.diag(np.arange(2,12))[::-1]
x[np.diag_indices_from(x[::-1])] = np.arange(2,12)
x2 =np.arange(x.size).reshape(x.shape)


