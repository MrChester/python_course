import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self, pi=math.pi):
        print(int(pi * self.radius ** 2))

new_circle = Circle(10)
new_circle.area()
