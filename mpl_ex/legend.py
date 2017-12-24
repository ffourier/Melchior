#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label = 'Philadelphia')
ax.plot([1, 2, 3, 4], [30, 23, 13, 4], label = 'Boston')
ax.set(ylabel = 'Temperature (deg C)', xlabel = 'Time', title = 'A tale of two cities')
ax.legend()
plt.show()
