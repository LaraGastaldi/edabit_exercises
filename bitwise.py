def binarizar(x, tam=8):
    bina = str(bin(x)[2:])
    if len(bina) < 8:
        rest = 8 - len(bina)
        bina = rest * "0" + bina
    return str(bina)

def desbinarizar(x):
    dec = int(x, 2)
    return dec

print(desbinarizar("0001111"))

def bitwise_and(n1, n2):
    n1, n2 = binarizar(n1), binarizar(n2)
    novo = []

    for idx, num in enumerate(n1):
        if num == n2[idx] and num == "1":
            novo.append("1")
        else:
            novo.append("0")

    novo = "".join(novo)
    return desbinarizar(novo)

print(bitwise_and(6, 23))


def bitwise_or(n1, n2):
    n1, n2 = binarizar(n1), binarizar(n2)
    novo = []

    for idx, num in enumerate(n1):
        if num == "1" or n2[idx] == "1":
            novo.append("1")
        else:
            novo.append("0")

    novo = "".join(novo)
    return desbinarizar(novo)

print(bitwise_or(6, 23))


def bitwise_xor(n1, n2):
    n1, n2 = binarizar(n1), binarizar(n2)
    novo = []

    for idx, num in enumerate(n1):
        if (n2[idx] == "1" and n2[idx] != num) or (num == "1" and num != n2[idx]):
            novo.append("1")
        else:
            novo.append("0")

    novo = "".join(novo)
    return desbinarizar(novo)

print(bitwise_xor(7, 12))