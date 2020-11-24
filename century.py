def century_from_year(n):
    century = (n/100)
    if century - int(century) != 0:
        century += 1
    return int(century)

print(century_from_year(200))