def return_unique(lst):
    return [i for i in lst if lst.count(i) == 1]

print(return_unique([1, 9 ,8, 8, 7, 6, 1, 6]))