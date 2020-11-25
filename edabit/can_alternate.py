def can_alternate(s):
    if len(s) % 2 == 0:
        if s.count("0") == s.count("1"):
            return True
        return False
    else:
        if s.count("0") == s.count("1")-1 or s.count("0") == s.count("1")+1:
            return True
        return False