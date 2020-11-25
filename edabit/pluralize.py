def pluralize(lst):
    nova = set(lst)
    resp = set()
    print(nova)
    for item in nova:
        print(item)
        if lst.count(item) > 1:
            resp.add(item+"s")
        else:
            resp.add(item)
    return resp

print(pluralize(["cow", "pig", "cow", "cow"]))