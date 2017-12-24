#!/usr/local/bin/python3.6

from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

lc = LineCollection ([[(4, 10), (16, 10)],
		      [(2, 2), (10, 15), (6, 7)],
		      [(14, 3), (1, 1), (3, 5)]])

lc.set_color(['r', 'blue', (0.2, 0.9, 0.3)])
lc.set_linewidth([4, 3, 6])
ax.add_collection(lc)
ax.set_xlim(0, 18)
ax.set_ylim(0, 18)
plt.show()
