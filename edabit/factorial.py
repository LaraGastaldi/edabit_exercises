def factorial(n):
    resp = 1
    for num in range(1, n+1):
        resp *= num
    return resp

print(factorial(5))