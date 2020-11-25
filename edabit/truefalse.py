def integer_boolean(n):
    result = []
    for num in n:
        if num == "1":
            result.append(True)
        else:
            result.append(False)
    return result