#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt
import numpy as np

data = [('apples', 2), ('oranges', 3), ('peaches', 1)]
fruit, value = zip(*data)

print(fruit)

fig, ax = plt.subplots()
x = np.arange(len(fruit))
ax.bar(x, value, align = 'center', color = 'gray')
ax.set(xticks = x, xticklabels = fruit)
plt.show()
