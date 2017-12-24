#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

xs, ys = np.mgrid[:4, 9:0:-1]

# codes for various markers
markers = [".", "+", ",", "x", "o", "D", "d", "", "8", "s", "p", "*", "|", "_", "h", "H", 0, 4, "<", "3",
	    1, 5, ">", "4", 2, 6, "^", "2", 3, 7, "v", "1", "None", None, " ", ""]

# descriptions of marker appearances
descripts = ["point", "plus", "pixel", "cross", "circle", "diamond", "thin diamond", "",
	     "octagon", "square", "pentagon", "star", "vertical bar", "horizontal bar", "hexagon 1",
	     "hexagon 2", "tick left", "caret left", "triangle left", "tri left", "tick right", "caret right",
    	     "triangle right", "tri right", "tick up", "caret up", "triangle up", "tri up", "tick down", "caret down",
	     "triangle down", "tri down", "Nothing", "Nothing", "Nothing", "Nothing"]

# create a figure with one subplot
fig, ax = plt.subplots(1, 1, figsize = (7.5, 4))

# populate the figure with markers and their descriptions
for x, y, m, d in zip(xs.T.flat, ys.T.flat, markers, descripts):
	ax.scatter(x, y, marker = m, s = 100)
	ax.text(x + 0.1, y - 0.1, d, size = 14)

# make axes invisible 
ax.set_axis_off()
plt.show()
