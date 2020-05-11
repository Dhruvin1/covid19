from random import randint
from random import choice
import settings
import math


class Liearwalk():
    """ A class to generate random walks."""

    def __init__(self, x=0, y=0):
        """Initiate attributes of a walk"""
        # All walks start at  (x,y)
        self.is_infected = False
        self.x_values = []
        self.y_values = []
        self.infection = False
        self.infected_days = 0
        self.dead = False
        self.angle = randint(0,360)
        self.speed = 5
        self.x_values.append(x)
        self.y_values.append(y)

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        #while len(self.x_values) < settings.WALK_DAYS:

        # Decide which direction to go and how far to go in that direction
        # x_direction = choice([-1,1])
        # x_distance = choice([0,1,2,3])
        # x_step = x_direction*x_distance
        #
        # y_direction = choice([-1,1])
        # y_distance = choice([0,1,2,3])
        # y_step = y_direction*y_distance

        # Calculate new position
        x = self.x_values[-1] + int(self.speed * math.cos(math.radians(self.angle)))
        y = self.y_values[-1] + int(self.speed * math.sin(math.radians(self.angle)))

        if abs(x) > settings.X_LIMIT:
            x = self.x_values[-1]
            if self.angle >= 0:
                self.angle = 180 - self.angle
            else:
                self.angle = -180 - self.angle

        if abs(y) > settings.Y_LIMIT:
            y = self.y_values[-1]
            self.angle = -self.angle

        self.x_values.append(x)
        self.y_values.append(y)