def encrypt(word):
    dici = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    word = list(word)
    word.reverse()
    word = "".join(word)
    palavra = ""
    for letra in word:
        if letra in "aeiou":
            palavra += dici[letra]
        else:
            palavra += letra
    palavra += "aca"
    return palavra


print(encrypt("apple"))