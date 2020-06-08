class Coordinate:
    x = 0.0
    y = 0.0

def is_in_square(square1, side1, square2, side2):
    left1 = square1.x - (side1/2)
    right1 = square1.x + (side1/2)
    top1 = square1.y - (side1/2)
    bottom1 = square1.y + (side1/2)
    
    left2 = square2.x - (side2/2)
    right2 = square2.x + (side2/2)
    top2 = square2.y - (side2/2)
    bottom2 = square2.y + (side2/2)
    
    if (left1 <= right2 and right1 >= left2 and
     top1 >= bottom2 and bottom1 <= top2):
        return True
    elif (left1 <= right2 and right1 >= left2):
        return True
    elif (top1 >= bottom2 and bottom1 <= top2):
        return True
    else:
        return False