import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the pointsself.

rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
