# test cases
# Circle(Point(10, 10), 30) --> 188.495559
# Circle(Point(25, -70), 30) --> 188.495559
# Circle(Point(-15, 5), 0) --> 0
# Circle(Point(-15, 5), 12.5) --> 78.539816

from math import pi

def circle_circumference(circle):
    return round(2*pi*circle.radius, 6)
