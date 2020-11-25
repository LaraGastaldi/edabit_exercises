def find_vertex(a, b, c):
    x = -b/(2*a)
    y = a*x**2+b*x+c
    if x == -0: x = abs(x)
    return [x, y]

print(find_vertex(1, 0, 25))
print(find_vertex(-1, 0, 25))
print(find_vertex(1, 10, 4))