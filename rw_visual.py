from random_walk import Randomwalk
from linear_walk import Liearwalk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from random import randint
import numpy as np
import settings

infections = 0
dead = 0
recovered = 0
NODE_ELEMENT = range(settings.NODES)
colors = cm.rainbow(np.linspace(0, 1, settings.NODES))
# Infected is array of two with white and black
colors_infected=cm.Greys(np.linspace(0,1,2))
fig, ax = plt.subplots()

# give random positions to settings.NODES
for j in range(settings.NODES):
    if settings.PATTERN == 'linear':
        NODE_ELEMENT[j] = Liearwalk(x=randint(-1*settings.X_LIMIT,settings.X_LIMIT),
                                     y=randint(-1*settings.Y_LIMIT,settings.Y_LIMIT))
    else:
        NODE_ELEMENT[j] = Randomwalk(x=randint(-1 * settings.X_LIMIT, settings.X_LIMIT),
                                     y=randint(-1 * settings.Y_LIMIT, settings.Y_LIMIT))

# Initial infection
print('Initiate infections are:',settings.NODES/10)
for i in range (settings.NODES/10):
    NODE_ELEMENT[i].is_infected = True
    colors[i] = colors_infected[1]

# walk each node for iteration specified in WALK_DAYS
for i in range(settings.WALK_DAYS):
    current_pos = [(0,0) for a in range(settings.NODES)]
    for j in range(settings.NODES):
        NODE_ELEMENT[j].fill_walk()
        current_pos[j] = (NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1])
    for j in range(settings.NODES):
        if NODE_ELEMENT[j].is_infected == True:
            #if (NODE_ELEMENT[j].x_values[-1],NODE_ELEMENT[j].y_values[-1])
            vul_pos = []
            for vul_x in range(NODE_ELEMENT[j].x_values[-1]-1,NODE_ELEMENT[j].x_values[-1]+2):
                for vul_y in range(NODE_ELEMENT[j].y_values[-1] - 1, NODE_ELEMENT[j].y_values[-1] + 2):
                    vul_pos.append((vul_x,vul_y))
            indices = [indice for indice, node_pos in enumerate(current_pos) if node_pos in vul_pos and node_pos!=j]
            for d in indices:
                NODE_ELEMENT[d].is_infected = True
                colors[d] = colors_infected[1]
    if settings.VISUALIZATION == True:
        for j in range(settings.NODES):
            ax.scatter(NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1], c=colors[j], s=20)
        plt.pause(0.02)
        if settings.LEAVE_TRACE == False:
            plt.cla()
        #ax.scatter(NODE_ELEMENT[j].x_values,NODE_ELEMENT[j].y_values,c=np.random.rand(3,),s=20)
    # for i in range(len(NODE_ELEMENT[0].x_values)):
    #     for j in range(settings.NODES):
    #         ax.scatter(NODE_ELEMENT[j].x_values[i], NODE_ELEMENT[j].y_values[i])
    #         plt.pause(0.05)


for j in range(settings.NODES):
    if settings.VISUALIZATION == False:
        ax.scatter(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j], s=20)
        #ax.plot(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j])
#    if NODE_ELEMENT[j].is_infected == True:
#        infection +=1
#print("Total infections were:", infection)

plt.show()
