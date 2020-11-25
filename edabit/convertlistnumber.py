def to_list(num):
    lst = [int(i) for i in str(num)]
    return lst


def to_number(lst):
    newlst = [str(i) for i in lst]
    return "".join(newlst)