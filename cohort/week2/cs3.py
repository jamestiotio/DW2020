from math import sqrt

class Coordinate:
    x = 0.0
    y = 0.0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)
    side2 = sqrt((p3.x-p2.x)**2 + (p3.y-p2.y)**2)
    side3 = sqrt((p3.x-p1.x)**2 + (p3.y-p1.y)**2)

    s = (side1 + side2 + side3) / 2
    area = sqrt(s * (s-side1) * (s-side2) * (s-side3))
    return round(area, 2)