import numpy as np
import matplotlib.pyplot as plt

def get_all_figures():
    return [plt.figure(i) for i in plt.get_fignums()]


fig1, ax1 = plt.subplots()
print(id(fig1))
print(id(plt.gcf()))

fig2, ax2 = plt.subplots()
print(id(fig2))
print(id(fig2)==id(plt.gcf())) #current figure has changed to fig2

print(plt.get_fignums())

print(get_all_figures())

plt.close('all')
print(get_all_figures())
