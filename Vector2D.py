import random
import math


class Vector2D:
    """Class representing a 2D Vector"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%s, %s]" % (self.x, self.y)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitudeSquared(self):
        return self.x ** 2 + self.y ** 2

    @staticmethod
    def zero():
        return Vector2D(0, 0)

    @staticmethod
    def rnd():
        return Vector2D(random.random(), random.random())
