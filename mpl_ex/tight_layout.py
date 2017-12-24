#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

def example_plot(ax):
	ax.plot([1, 2])
	ax.set_xlabel('x-label', fontsize = 16)
	ax.set_ylabel('y-label', fontsize = 8)
	ax.set_title('Title', fontsize = 24)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2)
example_plot(ax1)
example_plot(ax2)
example_plot(ax3)
example_plot(ax4)

# Enable fig.tight_layout to compare...
fig.tight_layout()

plt.show()
