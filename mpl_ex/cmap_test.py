#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)
z = np.random.random((10, 10))
axes[0,0].imshow(z, interpolation = 'none', cmap = 'nipy_spectral')
axes[0,1].imshow(z, interpolation = 'none', cmap = 'inferno')
axes[1,0].imshow(z, interpolation = 'none', cmap = 'bone')
axes[1,1].imshow(z, interpolation = 'none', cmap = 'Wistia')

plt.show()
