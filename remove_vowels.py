def remove_vowels(txt):
    new = [i for i in txt if i not in "aeiou" and i not in "AEIOU"]
    print(new)
    return "".join(new)

print(remove_vowels("Hello I am Lara"))