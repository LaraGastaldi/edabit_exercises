def amplify(x):
    lst = []
    for num in range(1, x+1):
        if num % 4 == 0:
            lst.append(num*10)
        else:
            lst.append(num)
    return lst