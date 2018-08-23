
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a random walk, and plot the points
rw = RandomWalk(50000)
rw.fill_walk()
plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.show()
