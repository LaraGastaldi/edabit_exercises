def correct_spacing(string):
    new = ""
    ant = False
    for idx, letra in enumerate(string):
        if letra == " ":
            if ant or idx == len(string)+1:
                continue
            else:
                new += letra
                ant = True
        else:
            new += letra
            ant = False
    return new

print(correct_spacing("(   eu    gosto   de pirulito  "))