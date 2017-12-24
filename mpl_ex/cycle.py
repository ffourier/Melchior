#!/usr/local/bin/python3.6

import matplotlib as mpl
from matplotlib.rcsetup import cycler
import matplotlib.pyplot as plt
import numpy as np


mpl.rc('axes', prop_cycle = cycler('color', ['r', 'orange', 'c', 'y']) +
			    cycler('hatch', ['x', 'xx-', '+O.', '*']))

x = np.array([0.4, 0.2, 0.5, 0.8, 0.6])
y = [0, -5, -6, -5, 0]
plt.fill(x+1, y)
plt.fill(x+2, y)
plt.fill(x+3, y)
plt.fill(x+4, y)

plt.show()
