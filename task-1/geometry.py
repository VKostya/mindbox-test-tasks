import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        """Calculate area of a figure"""

    @abstractmethod
    def validate_figure(self, *args):
        """Validates if __init__ params are correct"""


class Circle(Figure):
    def validate_figure(self, *args):
        if args[0] <= 0:
            raise ValueError("Radius should be a positive number or greater than null")

    def __init__(self, radius):
        self.validate_figure(radius)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2


class RightTriangleMixin:
    def is_right_triangle(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


class Triangle(Figure, RightTriangleMixin):
    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def validate_figure(self, a, b, c):
        if any(side <= 0 for side in [a, b, c]) or not self.is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle dimensions")

    def __init__(self, a, b, c):
        self.validate_figure(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
