#!/usr/local/bin/python3.6

import numpy as np
import matplotlib.pyplot as plt

index = range(2000, 2017)
divs = [0.68, 0.76, 0.76, 0.92, 1.12, 1.32, 1.52, 1.68, 1.80, 1.80, 1.88,
	2.08, 2.28, 2.48, 2.68, 2.92, 3.12]

fig, ax = plt.subplots(figsize = (10, 6))

test = []
for i in range(2000, 2017):
	test.append('hi')

bars = ax.bar(index, divs, color = 'green', edgecolor = 'black')
plt.xticks(index, test, rotation = 'vertical')

fig.autofmt_xdate()

for bar, div in zip(bars, divs):
	height = bar.get_height()
	ax.text(bar.get_x() + bar.get_width()/2, height, str(div), ha = 'center', va = 'bottom')

plt.show()
