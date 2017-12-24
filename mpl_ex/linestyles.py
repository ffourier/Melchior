#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.2)

plt.plot(t, t**0.5, 'r--', t, t, 'k^')
plt.show()
