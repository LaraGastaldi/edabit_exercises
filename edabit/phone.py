def dial(txt):
    alpha = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    resp = ""
    for letter in txt:
        if letter.isalpha():
            letter = letter.lower()
            for idx, letra in enumerate(alpha):
                if letter in letra:
                    resp += str(idx+2)
        else:
            resp += letter
    return resp

print(dial("1-800-HOTLINEBLING"))