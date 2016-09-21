import math

class Point:
    def points(self, x=(0, 0)):
        return x

class Polyline:
    def __init__(self, polyList=[]):
        self.polyList = polyList

    def calcLine(self, polyline):
        return

class Polygon:
    def __init__(self):
        array = []
    def makePoly(self, array):
        print 'ayy'

class Point1:
    x = 0.0
    y = 0.0
    def __init__(self, x= 0.0, y=0.0):
                self.x = x
                self.y = y

    def distance(self, point):
        return math.sqrt((point.x-self.x)**2+(point.y-self.y)**2)

p1=Point1()
p1.x = 1
p1.y = 2
p2 = Point1(3, 4)
print p1.distance(p2)

test = Point()
print test.points((3, 4))


