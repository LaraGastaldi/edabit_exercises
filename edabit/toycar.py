import math
def cars(wheel, body, figure):
    if wheel < 4 or body < 1 or figure < 2:
        return 0
    else:
        wheel /= 4
        figure /= 2
    return math.floor(min(wheel, body, figure))

print(cars(2, 48, 76))
print(cars(43, 15, 87))
print(cars(88, 37, 17))