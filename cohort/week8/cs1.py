import math

class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __eq__(self, other):
        return bool(self.x == other.x and self.y == other.y)