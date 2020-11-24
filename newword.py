def word_builder(lst1, lst2):
    new = ""
    for num in range(len(lst1)):
        new += lst1[lst2[num]]
    return new

print(word_builder(["g", "e", "o"], [1, 0, 2]))
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))