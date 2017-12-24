#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')

t = np.linspace(0, 2 * np.pi, 150)
x1, y1 = np.cos(t), np.sin(t)
x2, y2 = 2 * x1, 2 * y1

colors = ['darkred', 'darkgreen']

fig, ax = plt.subplots(1, 1)

ax.plot(x1, y1, color = colors[0], lw = 3, label = "Inner")
ax.plot(x2, y2, color = colors[1], lw = 3, label = "Outer")

ax.axis("equal")
ax.margins(0.05)

ax.legend(loc = 'best')

plt.show()
