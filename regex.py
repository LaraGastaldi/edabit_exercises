import re

def has_digit(txt):
    x = re.search("^.*[0-9].*$", txt)
    if x:
        return True
    return False

print(has_digit("Ola l1nda"))