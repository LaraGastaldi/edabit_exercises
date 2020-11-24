def jazzify(lst):
    new = []
    for accord in lst:
        if accord[-1] != "7":
            new.append(accord+"7")
        else:
            new.append(accord)
    return new