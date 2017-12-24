#!/usr/local/bin/python3.6

from matplotlib.collections import StarPolygonCollection
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)

collection = StarPolygonCollection(5,
				   offsets = [(0.5, 0.5)],
			           sizes = (150, ),
				   transOffset = ax.transData)
ax.add_collection(collection)
plt.show()
