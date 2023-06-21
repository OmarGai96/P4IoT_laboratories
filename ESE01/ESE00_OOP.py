from SquareManager import *
from Point import *
from Point3D import *
from Line import *

if __name__=="__main__":
    #Exercise 0
    sm=SquareManager(5)

    print('Area: ', sm.area())
    print('Perimeter: ', sm.perimeter())
    print('Diagonal: ', sm.diagonale())

    #Exercise 1
    a=Point(7,1)
    b=Point(1,1)
    print(f'distance from a to b is: {a.distance(b)}')
    
    a.move(8,2)
    print(f"Move a in ({a.getx()}, {a.gety()})")

    c=Point3D(1,2,1)
    print(f"Point 3D is in position ({c.getx()},{c.gety()},{c.getz()})")
    #Exercise 2
    l1 = Line(3,2)

    a=Point(0,1)
    b=Point(3,1)
    l2=Line(0,0)
    length= l2.line_from_points(a,b)
    print(length)
    
