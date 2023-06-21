import math
class SquareManager:
    def __init__(self, sideLenght):
        self.sideLenght=sideLenght
    def area(self):
        return self.sideLenght**2
        
    def perimeter(self):
        return self.sideLenght*4

    def diagonale(self):
        return self.sideLenght*math.sqrt(2)
