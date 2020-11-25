months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
import re

def fiscal_code(person):
    # SURNAME
    surname = person["surname"]
    surname = surname.upper()
    conso = [n for n in surname if n not in "AEIOU"]
    conso = "".join(conso)
    if len(conso) < 3:
        if len(surname) < 3:
            surname += "X"
        else:
            vogal = re.sub(conso[0], "", surname)[:1]
            surname = conso + vogal
    else:
        surname = conso[:3]
    # print(surname)


    # NAME
    name = person["name"]
    name = name.upper()
    conso = [c for c in name if c not in "AEIOU"]
    conso = "".join(conso)
    if len(conso) == 3:
        name = conso
    elif len(conso) > 3:
        name = conso[0]+conso[2]+conso[3]
    elif len(name) < 3:
        for n in name:
            if n in "AEIOU":
                letra = n
                break
        name = conso+letra+"X"
    elif len(conso) < 3:
        for n in name:
            if n in "AEIOU":
                letra = n
                break
        name = conso+letra
    # print(name)


    # DATA DE NASC E GENERO
    nasc = person["dob"].split("/")
    ano = nasc[2][2:4]
    mes = months[nasc[1]]
    # homem
    dia = 0
    if person["gender"] == "M":
        if int(nasc[0]) < 10:
            dia = "0"+nasc[0][:1]
        else:
            dia = nasc[0]
    else:
        dia = int(nasc[0])+40
    dia = str(dia)
    
    # COMPLETO
    return surname+name+ano+mes+dia



print(fiscal_code({ "name": "Brendan", "surname": "Eich", "gender": "M", "dob": "1/12/1961"}))
print(fiscal_code({ "name": "Helen", "surname": "Yu", "gender": "F", "dob": "1/12/1950"}))
print(fiscal_code({ "name": "Al", "surname": "Capone", "gender": "M", "dob": "17/1/1899"}))
print(fiscal_code({ "name": "Mickey", "surname": "Mouse", "gender": "M", "dob": "16/1/1928"}))
print(fiscal_code({ "name": "Marie", "surname": "Curie", "gender": "F", "dob": "7/11/1867"}))