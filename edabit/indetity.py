def id_mtrx(n):
    if not isinstance(n, int):
        return "Error"
    listinha = [[] for i in range(abs(n))]
    if n > 0:
        for linha in range(n):
            for coluna in range(n):
                if coluna == linha:
                    listinha[linha].append(1)
                else:
                    listinha[linha].append(0)
    else:
        n = abs(n)
        cont = n - 1
        for linha in range(n):
            for coluna in range(n):
                if coluna == cont:
                    listinha[linha].append(1)
                else:
                    listinha[linha].append(0)
            cont -= 1
    return listinha

print(id_mtrx(-3))