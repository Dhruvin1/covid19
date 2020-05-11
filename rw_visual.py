from random_walk import Randomwalk
from linear_walk import Liearwalk
import matplotlib.pyplot as plt
from numpy.random import choice
import matplotlib.cm as cm
from random import randint
import numpy as np
import settings

infections = 0
dead = 0
recovered = 0
fate = [0,1]
prob = [1-settings.MORTALITY, settings.MORTALITY]
NODE_ELEMENT = range(settings.NODES)
colors = cm.rainbow(np.linspace(0, 1, settings.NODES))
# Infected is array of two with white and black
colors_infected=cm.Greys(np.linspace(0,1,3))
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
    NODE_ELEMENT[i].infection = True
    NODE_ELEMENT[i].infected_days = 1
    colors[i] = colors_infected[2]
    infections += 1

# walk each node for iteration specified in WALK_DAYS
for i in range(settings.WALK_DAYS):
    current_pos = [(0,0) for a in range(settings.NODES)]
    for j in range(settings.NODES):
        if NODE_ELEMENT[j].dead:
            continue
        NODE_ELEMENT[j].fill_walk()
        current_pos[j] = (NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1])
    for j in range(settings.NODES):
        if NODE_ELEMENT[j].dead:
            continue
        if NODE_ELEMENT[j].is_infected:
            #if (NODE_ELEMENT[j].x_values[-1],NODE_ELEMENT[j].y_values[-1])
            vul_pos = []
            for vul_x in range(NODE_ELEMENT[j].x_values[-1]-1,NODE_ELEMENT[j].x_values[-1]+2):
                for vul_y in range(NODE_ELEMENT[j].y_values[-1] - 1, NODE_ELEMENT[j].y_values[-1] + 2):
                    vul_pos.append((vul_x,vul_y))
            indices = [indice for indice, node_pos in enumerate(current_pos) if (node_pos in vul_pos and node_pos!=j)]
            for d in indices:
                if not NODE_ELEMENT[d].infection:
                    NODE_ELEMENT[d].is_infected = True
                    NODE_ELEMENT[d].infection = True
                    NODE_ELEMENT[d].infected_days = 1
                    colors[d] = colors_infected[2]
                    infections += 1
            NODE_ELEMENT[j].infected_days += 1
            if NODE_ELEMENT[j].infected_days > settings.INFECTION_DAYS:
                colors[j] = colors_infected[0]
                NODE_ELEMENT[j].is_infected = False
                if choice(fate,p=prob) == 1:
                    NODE_ELEMENT[j].dead = True
                    dead += 1
                else:
                    recovered += 1


    if settings.VISUALIZATION:
        for j in range(settings.NODES):
            ax.scatter(NODE_ELEMENT[j].x_values[-1], NODE_ELEMENT[j].y_values[-1], c=colors[j], s=50,
                       label=' Days={}\n Infections={}\n Deaths={}\n Recovered={}\n'.format(i,infections,dead, recovered))
            # ax[1].scatter(i,infections, c=colors_infected[1], label="infections")
            # ax[1].scatter(i, dead, c=colors_infected[2],label="dead")
            # ax[1].scatter(i, recovered ,c=colors_infected[0], label="recovered")
            # ax[1].plot(i, infections)
            # ax[1].plot(i, dead)
            # ax[1].plot(i, recovered)
            if j == 0:
                ax.legend()
        plt.pause(0.005)

        if not settings.LEAVE_TRACE:
            ax.clear()

        #ax.scatter(NODE_ELEMENT[j].x_values,NODE_ELEMENT[j].y_values,c=np.random.rand(3,),s=20)
    # for i in range(len(NODE_ELEMENT[0].x_values)):
    #     for j in range(settings.NODES):
    #         ax.scatter(NODE_ELEMENT[j].x_values[i], NODE_ELEMENT[j].y_values[i])
    #         plt.pause(0.05)


for j in range(settings.NODES):
    if not settings.VISUALIZATION:
        ax.scatter(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j], s=50)
        #ax[1].scatter(1,1, c=colors_infected[1], label="To be developed")

        #ax.plot(NODE_ELEMENT[j].x_values, NODE_ELEMENT[j].y_values, c=colors[j])
#    if NODE_ELEMENT[j].is_infected == True:
#        infection +=1
#print("Total infections were:", infection)

plt.show()
