#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

plt.style.use('classic')

# Generate random data with different rnages...
data1 = np.random.random((10, 10))
data2 = 2 * np.random.random((10, 10))
data3 = 3 * np.random.random((10, 10))

# Set up our figures and axes...
fig, axes = plt.subplots(ncols = 3, figsize = plt.figaspect(0.5))
fig.tight_layout() # Make the subplots fill up the figure a bit more...
cax = fig.add_axes([0.25, 0.1, 0.55, 0.03]) # Add an axes for the colorbar

im1 = axes[0].imshow(data1, interpolation = 'nearest', vmin = 0.0, vmax = 3.0)
im2 = axes[1].imshow(data2, interpolation = 'nearest', vmin = 0.0, vmax = 3.0)
im3 = axes[2].imshow(data3, interpolation = 'nearest', vmin = 0.0, vmax = 3.0)

fig.colorbar(im1, cax = cax, orientation = 'horizontal')
plt.show()
