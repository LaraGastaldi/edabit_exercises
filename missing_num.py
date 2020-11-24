def missing_num(lst):
    lst.sort()
    anterior = lst[0]
    missing = None
    for num in lst:
        if num == lst[0]:
            continue
        else:
            if num != (anterior + 1):
                missing = num - 1
        anterior = num
    if missing == None:
        if lst[0] == 2:
            missing = 1
        else:
            missing = 10
    return missing

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))