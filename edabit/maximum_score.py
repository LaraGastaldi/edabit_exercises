def maximum_score(tile_hand):
    total = 0
    for dici in tile_hand:
        total += dici["score"]
    return total