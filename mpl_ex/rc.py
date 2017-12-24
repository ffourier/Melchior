#!/usr/local/bin/python3.6

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcdefaults()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot([1, 2, 3, 4])

mpl.rc('lines', linewidth = 2, linestyle = '-.')

ax2.plot([1, 2, 3, 4])
plt.show()
