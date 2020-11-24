def convert_cartesian(x, y):
    lst = []
    for idx, num in enumerate(x):
        lst.append([num, y[idx]])
    return lst