def society_name(friends):
    letters = []
    for friend in friends:
        letters.append(friend[0])
    letters.sort()
    letters = "".join(letters)
    letters.upper()
    return letters