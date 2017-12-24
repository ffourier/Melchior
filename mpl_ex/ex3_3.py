#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-5.0, 5.0, 0.1)
a = np.sinc(t)
plt.plot(t, a, linestyle = 'dotted', color = 'red', marker = 'D', mec = 'green', mfc = 'yellow')

plt.show()
