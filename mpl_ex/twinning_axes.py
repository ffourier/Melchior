#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots(1, 1)
ax1.plot([1, 2, 3, 4], [1, 2, 3, 4])
ax2 = ax1.twinx()
ax2.scatter([1, 2, 3, 4], [60, 50, 40, 30])
ax1.set(xlabel = 'X', ylabel = 'First scale')
ax2.set(ylabel = 'Other scale')
plt.show()
