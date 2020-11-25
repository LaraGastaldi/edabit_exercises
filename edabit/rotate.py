def rotate(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    mat.reverse()
    resp = []
    for linha in range(linhas):
        line = []
        for coluna in range(colunas):
            line.append(mat[coluna][linha])
        resp.append(line)
    return resp

print(rotate([[1, 2], [3, 4]]))
# 1 2
# 3 4

# 3 1
# 4 2