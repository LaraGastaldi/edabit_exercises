def tallest_skyscraper(lst):
    linhas = len(lst)
    colunas = len(lst[0])
    for linha in range(linhas):
        for coluna in range(colunas):
            if lst[linha][coluna] == 1:
                return linhas - linha

print(tallest_skyscraper([[0, 1, 0, 0],[0, 1, 0, 0],[0, 1, 1, 0],[1, 1, 1, 1]]))