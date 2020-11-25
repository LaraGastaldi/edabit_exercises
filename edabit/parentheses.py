def split(txt):
    palavra = ""
    conjunto = []
    match = 0
    for letra in txt:
        if letra == "(":
            match += 1
            palavra += letra
        elif letra == ")":
            match -= 1
            if match == 0:
                palavra += letra
                conjunto.append(palavra)
                palavra = ""
            else:
                palavra += letra
    return conjunto

print(split("(()) () ()"))