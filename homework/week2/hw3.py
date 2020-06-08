import math
def area_vol_cylinder(radius, length):
    pi = math.pi
    area = pi * (radius ** 2)
    volume = area * length
    return (round(area, 2), round(volume, 2))