def correct_stream(user, correct):
    resp = []
    for idx, word in enumerate(user):
        if word == correct[idx]:
            resp.append(1)
        else:
            resp.append(-1)
    return resp