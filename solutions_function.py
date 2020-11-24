def solutions(a, b, c):
    delta = pow(b,2) - 4 * a * c
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2

print(solutions(1, 0, -1))