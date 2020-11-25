def sum_of_evens(lst):
    num = 0
    for linha in lst:
        for coluna in linha:
            if coluna % 2 == 0:
                num += coluna
    return num