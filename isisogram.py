def is_isogram(word):
    word = word.lower()
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True