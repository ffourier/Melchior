#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])

# Manually set ticks and tick labels *on the x-axis* (note ax.xaxis.set, not ax.set!)
ax.xaxis.set(ticks = range(1, 5), ticklabels = [3, 100, -12, "foo"])

# Make the y-ticks a bit longer and go both in and out ...
ax.tick_params(axis = 'y', direction = 'inout', length = 10)

plt.show()
