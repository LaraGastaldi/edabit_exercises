def count_layers(rug):
    print(len(rug))
    if len(rug) <= 2:
        mid = 0
    else:
        mid = (len(rug)//2)
    
    last = None
    count = 0
    print(mid)
    for letter in rug[mid]:
        if letter != last:
            print(letter)
            count += 1
            last = letter
    count = count - count//2
    return count

print(count_layers([
"AAAA", 
"ABBA", 
"AAAA"]))