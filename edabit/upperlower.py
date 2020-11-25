def steps_to_convert(string):
    countupper = 0
    countlower = 0
    for letter in string:
        if letter.isupper():
            countupper += 1
        else:
            countlower += 1
    return min(countupper, countlower)

print(steps_to_convert("aba"))