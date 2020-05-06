from random import choice
import settings


class Randomwalk():
    """ A class to generate random walks."""

    def __init__(self, x=0, y=0):
        """Initiate attributes of a walk"""
        # All walks start at  (x,y)
        self.is_infected = False
        self.x_values = []
        self.y_values = []
        self.infected_days = 0
        self.x_values.append(x)
        self.y_values.append(y)

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < settings.WALK_DAYS:

            # Decide which direction to go and how far to go in that direction
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            if x_step == 0 and y_step == 0:
                continue

            # Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            if abs(x) > settings.X_LIMIT:
                x = self.x_values[-1]

            if abs(y) > settings.Y_LIMIT:
                y = self.y_values[-1]

            self.x_values.append(x)
            self.y_values.append(y)