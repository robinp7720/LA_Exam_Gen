def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def poly_divmod(num, den):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shiftlen + 1):
        mult = num[-1] / divisor
        quot = [mult] + quot

        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num

def vielfachheit(poly, zero): 
    coeffs = [1, (-1) * zero]

    v = 0 
    b = poly_divmod(poly, coeffs)
    while b[1][0] == 0.0: 
        v += 1
        b = poly_divmod(b[0], coeffs)

    return v
