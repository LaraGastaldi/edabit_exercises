def freed_prisoners(prison):
    prisoners = []
    for n in prison:
        prisoners.append(1)

    def troca(prisao):
        for idx, cela in enumerate(prisao):
            if cela == 0:
                prisao[idx] = 1
            else:
                prisao[idx] = 0

    if prison[0] == 0:
        return 0

    contador = 0
    # Para cada cela na prisão
    for cell in prison:
        # Se for a primeira
        if contador == 0:
            prisoners[contador] = 0
            troca(prison)
        
        # Se não for a primeira
        else:
            # Se estive fechada, ignore
            if cell == 0:
                continue
            # Se estiver aberta, liberte
            else:
                prisoners[contador] = 0
                troca(prison)
        contador += 1
    
    return prisoners.count(0)

print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))