def XO(txt):
    txt = list(txt)
    count1 = txt.count("x")
    count1 += txt.count("X")
    count2 = txt.count("o")
    count2 += txt.count("O")

    if count1 == count2:
        return True
    return False

print(XO("xoxoxo"))
print(XO("xox"))