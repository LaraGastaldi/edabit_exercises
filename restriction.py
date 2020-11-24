def alphanumeric_restriction(string):
    def find_type(n):
        if n.isdigit():
            return "digit"
        elif n.isalpha():
            return "letter"
        else:
            return "especial"
    tipo = ""

    if string == "":
        return False

    for idx, letter in enumerate(string):
        if idx == 0:
            if find_type(letter) == "especial":
                return False
            tipo = find_type(letter)
        else:
            tipo2 = find_type(letter)
            if tipo != tipo2:
                return False
    return True

print(alphanumeric_restriction("B0ld"))