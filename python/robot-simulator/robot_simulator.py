# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
      return (self.x, self.y)

    def advance(self):
        axis = self.bearing % 2
        negative = -1 if self.bearing > axis else 1

        if axis == 0:
          self.x += negative
        else:
          self.y += negative

    def turn_right(self):
        self.bearing = (self.bearing-1) % 4

    def turn_left(self):
        self.bearing = (self.bearing+1) % 4

    def simulate(self, path):
        tokenLookup = {
          'L': Robot.turn_left,
          'R': Robot.turn_right,
          'A': Robot.advance,
        }
        if not all(c in tokenLookup.keys() for c in path):
          raise ValueError('Invalid path provided')

        map(lambda token: tokenLookup[token](self), path)
