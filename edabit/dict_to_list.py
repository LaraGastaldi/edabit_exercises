def dict_to_list(d):
    d = sorted(d)
    print(d)
    return [(x, d[x]) for x in d.key()]

print(dict_to_list({'D': 1, 'B': 2, 'C': 3}))