from linear_walk import Liearwalk
import matplotlib.pyplot as plt
from random import randint
import settings

NODE_ELEMENT = range(settings.NODES)
fig, ax = plt.subplots(2)

ax[1].scatter(100, 100, c=[0,0,0], s=20)
for j in range(settings.NODES):
    NODE_ELEMENT[j] = Liearwalk(x=randint(-1*settings.X_LIMIT,settings.X_LIMIT), y=randint(-1*settings.Y_LIMIT,settings.Y_LIMIT))
#for i in range(settings.WALK_DAYS):
for i in range(10):
    for j in range(settings.NODES):
        NODE_ELEMENT[j].fill_walk()
        ax[0].scatter(NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1], c=[0,0,0], s=20)
    ax[1].scatter(NODE_ELEMENT[0].x_values[-1], NODE_ELEMENT[0].y_values[-1], c=[0, 0, 0], s=20)
    plt.pause(0.02)
    ax[0].clear()
    #plt.cla()


print(NODE_ELEMENT[1].x_values)

#plt.savefig('/Users/dhruvins/Desktop/Plots/test_liearwalk.png')
plt.show()

