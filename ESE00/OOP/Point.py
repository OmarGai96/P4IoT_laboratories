import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distance(self, p):
        dist=math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return dist 

    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def getx(self):
        return self.x
    def gety(self):
        return self.y
