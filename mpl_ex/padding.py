#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = plt.figaspect(0.5))

ax1.plot([-10, -5, 0, 5, 10, 15], [-1.2, 2, 3.5, -0.3, -4, 1])
ax2.scatter([-10, -5, 0, 5, 10, 15], [-1.2, 2, 3.5, -0.3, -4, 1])

ax1.margins(x = 0.0, y = 0.1)
ax2.margins(0.05)

plt.show()
