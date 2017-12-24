#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize = (7, 7))
fig.subplots_adjust(wspace = 0.9, hspace = 0.7,
		    left = 0.125, right = 0.9,
		    top = 0.9, bottom = 0.1)

plt.show()
