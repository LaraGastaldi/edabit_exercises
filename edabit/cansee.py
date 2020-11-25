def can_see_stage(seats):
    linhas = len(seats)
    colunas = len(seats[0])
    anterior = 0

    for coluna in range(colunas):
        for linha in range(linhas):
            if linha == 0:
                anterior = seats[linha][coluna]
            else:
                if seats[linha][coluna] <= anterior:
                    return False
            anterior = seats[linha][coluna]
    return True

print(can_see_stage([[4, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 5, 4, 4], 
[6, 6, 7, 6, 5, 5]]))