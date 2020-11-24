def return_only_integer(lst):
    lista = []
    for num in lst:
        if not isinstance(num, bool):
            if isinstance(num, int):
                lista.append(num)
    return lista

print(return_only_integer([1]))