def replace_vowels(txt, ch):
    resp = ""
    for letter in txt:
        if letter in "aeiou":
            resp += ch
        else:
            resp += letter
    return resp

print(replace_vowels("ola tudo bem", "*"))