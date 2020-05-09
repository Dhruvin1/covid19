from linear_walk import Liearwalk
import matplotlib.pyplot as plt
from random import randint
import settings

NODE_ELEMENT = range(settings.NODES)
fig, ax = plt.subplots()

for j in range(settings.NODES):
    NODE_ELEMENT[j] = Liearwalk(x=randint(-1*settings.X_LIMIT,settings.X_LIMIT), y=randint(-1*settings.Y_LIMIT,settings.Y_LIMIT))
for i in range(settings.WALK_DAYS):
    for j in range(settings.NODES):
        NODE_ELEMENT[j].fill_walk()
        ax.scatter(NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1], c=[0,0,0], s=5)
    plt.pause(0.02)
    plt.cla()
plt.show()
