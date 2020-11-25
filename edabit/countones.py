def count_ones(num):
    cont = 0
    binary = str(bin(num))[2:]
    for letra in binary:
        if letra == "1":
            cont += 1
    return cont

print(count_ones(2))