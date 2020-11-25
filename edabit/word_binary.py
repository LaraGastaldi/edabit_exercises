def convert_binary(word):
    alpha0 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    resp = ""
    for letter in word:
        if letter.lower() in alpha0:
            resp += "0"
        else:
            resp += "1"
    return resp