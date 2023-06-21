from Point import *

class Line:
        
    def __init__(self,m,q):
        self.m = m
        self.q = q
        self.p1 = Point(0,0)
        self.p2 = Point(0,0)
        self.length = 0

    def line_from_points(self,a,b):
        self.p1 = a
        self.p2 = b
        self.length=self.p1.distance(self.p2)
        return self.length
