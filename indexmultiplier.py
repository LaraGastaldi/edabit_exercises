def index_multiplier(lst):
    inic = 0
    for idx, num in enumerate(lst):
        inic += num * idx
    return inic