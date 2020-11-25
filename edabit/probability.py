def probability(lst, n):
    percenttotal = 100 / len(lst)
    percent = 0
    for number in lst:
        if number >= n:
            percent += percenttotal
    return round(percent, 1)

print(probability([5, 1, 8, 9], 6))