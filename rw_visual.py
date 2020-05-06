from random_walk import Randomwalk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import randint
import numpy as np
import settings

infection = 0
NODE_ELEMENT = range(settings.NODES)
colors = cm.rainbow(np.linspace(0, 1, settings.NODES))
fig, ax = plt.subplots()

# give random positions to settings.NODES
for j in range(settings.NODES):
    NODE_ELEMENT[j] = Randomwalk(x=randint(-1*settings.X_LIMIT,settings.X_LIMIT), y=randint(-1*settings.Y_LIMIT,settings.Y_LIMIT))

# Initial infection
NODE_ELEMENT[0].is_infected = True
colors[0] = ([0.5,  0.5,  0.5,  0.5])

# walk each node for iteration specified in WALK_DAYS
for i in range(settings.WALK_DAYS):
    current_pos = [(0,0) for a in range(settings.NODES)]
    for j in range(settings.NODES):
        NODE_ELEMENT[j].fill_walk()
        current_pos[j] = (NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1])
    for j in range(settings.NODES):
        if NODE_ELEMENT[j].is_infected == True:
            #if (NODE_ELEMENT[j].x_values[-1],NODE_ELEMENT[j].y_values[-1])
            indices = [b for b, c in enumerate(current_pos) if c == (NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1]) and c!=j]
            for d in indices:
                NODE_ELEMENT[d].is_infected = True
                colors[d] = ([0.5,  0.5,  0.5,  0.5])
    for j in range(settings.NODES):
        if settings.VISUALIZATION == True:
            ax.scatter(NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1], c=colors[j], s=10)
            plt.pause(0.05)
        #ax.scatter(NODE_ELEMENT[j].x_values,NODE_ELEMENT[j].y_values,c=np.random.rand(3,),s=20)
    # for i in range(len(NODE_ELEMENT[0].x_values)):
    #     for j in range(settings.NODES):
    #         ax.scatter(NODE_ELEMENT[j].x_values[i], NODE_ELEMENT[j].y_values[i])
    #         plt.pause(0.05)

if settings.VISUALIZATION == False:
    for j in range(settings.NODES):
        ax.scatter(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j], s=10)
        #ax.plot(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j])
        if NODE_ELEMENT[j].is_infected == True:
            infection +=1
print("Total infections is:", infection)

plt.show()
