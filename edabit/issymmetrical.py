def is_symmetrical(n):
    lst = [int(i) for i in str(n)]
    lst2 = [int(i) for i in str(n)]
    lst2.reverse()
    if lst == lst2:
        return True
    return False

print(is_symmetrical(28682))