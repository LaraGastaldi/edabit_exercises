def clone(lst):
    lst2 = list(lst)
    lst.append(lst2)
    return lst

print(clone(["1", "2"]))