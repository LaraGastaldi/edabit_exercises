import math
def shift_to_right(num: int, divisor: int) -> int:
    return math.floor(num/pow(2, divisor))