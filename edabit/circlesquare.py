import math
def circle_or_square(rad, area):
    circun = 2*3.14*rad
    lado = math.sqrt(area)
    peri = lado * 4
    if circun > peri:
        return True
    return False