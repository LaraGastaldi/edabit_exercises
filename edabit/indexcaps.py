def index_of_caps(word):
    idxs = []
    for idx, letter in enumerate(word):
        if letter.isupper():
            idxs.append(idx)
    return idxs

print(index_of_caps("aLoR"))