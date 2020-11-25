# Enter your code here. Read input from STDIN. Print output to STDOUT

file = open("files/findsubword.txt")

inp = file.read()

inp = inp.split("\n")
import re, sys
# inp = sys.stdin.read().split("\n")
cont = False
queries = []
phrases = []
found = 0

for sentence in inp[1:]:
    if sentence.isdigit():
        cont = True
        continue
    if cont:
        queries.append(sentence)
    else:
        phrases.append(sentence)

foundlst = []

for querie in queries:
    for phrase in phrases:
        found += len(re.findall("[A-Za-z]+"+querie+"[A-Za-z]+",phrase))
    foundlst.append(found)

for num in foundlst:
    pass
    print(num)

file.close()