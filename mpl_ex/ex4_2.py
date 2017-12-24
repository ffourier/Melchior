#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

def my_plot(ax, x, y, lab):
	ax.spines['bottom'].set_position(('data', 0))	
	ax.bar(np.arange(len(x)), y, align = 'center', color = 'gray', lw = 1, edgecolor = 'black')
	ax.set(xticks = np.arange(len(x)), xticklabels = x)
	ax.set_ylabel(lab)
	ax.yaxis.set(ticks = range(min(y), max(y) + 1))
	ax.tick_params(axis = 'x', direction = 'inout', length = 7)
	ax.tick_params(axis = 'y', direction = 'in')


	
data = [('dogs', 4, 4), ('frogs', -3, 1), ('cats', 1, 5), ('goldfish', -2, 2)]
animals, friendliness, popularity = zip(*data)

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)

fig.subplots_adjust(hspace = 0)

my_plot(ax1, animals, friendliness, 'Friendliness')
my_plot(ax2, animals, popularity, 'Popularity')

plt.show()
