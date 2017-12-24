#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data

data = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))

fig, ax = plt.subplots()
im = ax.imshow(data, cmap = 'seismic', interpolation = 'nearest', vmin = -2, vmax = 2)
fig.colorbar(im)
plt.show()
