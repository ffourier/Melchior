#!/usr/local/bin/python3.6

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 3)

for ax in axes:
	ax.plot([-10, -5, 0, 5, 10, 15], [-1.2, 2, 3.5, -0.3, -4, 1])

axes[0].set_title('Normal Autoscaling', y = 0.7, x = 0.8)

axes[1].set_title('ax.axis("tight")', y = 0.7, x = 0.8)
axes[1].axis('tight')

axes[2].set_title('ax.axis("equal")', y = 0.7, x = 0.8)
axes[2].axis('equal')

plt.show()
