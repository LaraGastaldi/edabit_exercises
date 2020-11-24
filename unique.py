def unique(lst):
    newlst = [str(i) for i in lst]
    valor = [i for i in newlst if newlst.count(i) == 1]
    valor = "".join(valor)
    try:
        valor = int(valor)
    except:
        valor = float(valor)
    return valor

print(unique([3, 3, 3, 7.2, 3, 3]))