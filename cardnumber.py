def card_hide(card):
    final = card[-4:]
    restante = len(card)-4
    return restante*"*"+final

print(card_hide("8247943269482"))