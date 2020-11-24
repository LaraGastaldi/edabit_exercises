def leaderboards(lst):
    truescore = {}
    resp = []
    for dici in lst:
        truescore.update({dici["name"]: (dici["score"]+(dici["reputation"]*2))})
    truescore = sorted(truescore.items(), key=lambda x: x[1], reverse=True)
    for tupla in truescore:
        for dici in lst:
            if tupla[0] == dici["name"]:
                resp.append(dici)
    return resp

print(leaderboards([{ "name": "a", "score": 100, "reputation": 20 },{ "name": "b", "score": 90, "reputation": 40 },{ "name": "c", "score": 115, "reputation": 30 },]))