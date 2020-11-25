def cycle_length(lst, n):
    def swap(lista, pos1, pos2):
        valor1 = lista[pos1]
        valor2 = lista[pos2]

        lista[pos1] = valor2
        lista[pos2] = valor1
        return lista[pos1]

    position = lst.index(n)
    cont = 0
    while position+1 != n:
        n = swap(lst, position, n-1)
        position = lst.index(n)
        cont += 1
    
    return cont

print(cycle_length([1, 5, 4, 3, 2, 6], 4))