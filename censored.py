def uncensor(string, vwls):
    new = ""
    cont = 0
    for letter in string:
        if letter == "*":
            new += vwls[cont]
            cont += 1
        else:
            new += letter
    return new