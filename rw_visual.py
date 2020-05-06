from random_walk import Randomwalk
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import settings

NODES = 100
NODE_ELEMENT = range(NODES)

fig, ax = plt.subplots()

#Make a random walk
for j in range(NODES):
    NODE_ELEMENT[j] = Randomwalk(x=randint(-1*settings.X_LIMIT,settings.X_LIMIT), y= randint(-1*settings.Y_LIMIT,settings.Y_LIMIT))
    NODE_ELEMENT[j].fill_walk()
    ax.scatter(NODE_ELEMENT[j].x_values,NODE_ELEMENT[j].y_values,c=np.random.rand(3,),s=20)
# for i in range(len(NODE_ELEMENT[0].x_values)):
#     for j in range(NODES):
#         ax.scatter(NODE_ELEMENT[j].x_values[i], NODE_ELEMENT[j].y_values[i])
#         plt.pause(0.05)

plt.show()
