#!/usr/local/bin/python3.6

from matplotlib.collections import RegularPolyCollection
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
offsets = np.random.rand(20, 2)
collection = RegularPolyCollection(
	numsides = 5,
	sizes = (150, ),
	offsets = offsets,
	transOffset = ax.transData,
	)
ax.add_collection(collection)
plt.show()
