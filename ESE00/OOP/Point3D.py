from Point import *

class Point3D(Point):
    def __init__(self,x,y,z):
        Point.__init__(self,x,y)
        self.z=z

    def distance(self,p):
        dist=math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2 )
        return dist

    def move(self,dx,dy,dz):
        Point.move(self,dx,dy)
        self.z += dz

    def getz(self):
        return self.z
