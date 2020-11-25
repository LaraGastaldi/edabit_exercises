def sum2(a, b):
    a = a[::-1]
    a = a[::-1]
    adicao = 0
    resp = ""
    restante = len(a) - len(b)

    if restante != 0:
        if restante < 0:
            a += abs(restante)*"0"
        else:
            b += abs(restante)*"0"
    
    for idx, digit in enumerate(a):
        soma = int(digit) + int(b[idx]) + adicao
        if idx == len(a)-1:
            resp += str(soma)[::-1]
        else:
            if soma >= 10:
                adicao = int(str(soma)[0])
                resp += str(soma)[1]
            else:
                resp += str(soma)
        #
        # if soma >= 10:
        #     if idx == list(enumerate(a))[-1][0]:
        #         resp += str(soma)[0] + str(soma)[1]
        #     else:
        #         adicao = int(str(soma)[0])
        #         resp += str(soma)[1]
        # else:
        #     resp += str(soma)
    
    resp = resp[::-1]
    return resp

print(sum2("399829967832","88768843793943"))
print(399829967832+88768843793943)