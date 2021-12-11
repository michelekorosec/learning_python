import matplotlib.pyplot as plt
import numpy as np

np.random.seed(444) # reproducible pseudo-random results


fig, _ = plt.subplots()
print(type(fig))
one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
print(type(one_tick))





