def rearranged_difference(num):
    num = [int(n) for n in str(num)]
    nummax, nummin = sorted(num, reverse=True), sorted(num)
    nummax, nummin = int("".join(map(str, nummax))), int("".join(map(str, nummin)))
    return nummax - nummin

print(rearranged_difference(972882))