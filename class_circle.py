import math

class Circle:
    def __init__(self, r):
        self.area = math.pi * r * r

circle = Circle(3)
print(circle.area)