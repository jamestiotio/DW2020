def gcd(a, b):
    d = 0
    while (a % 2 == 0) and (b % 2 == 0):
        a = a / 2
        b = b / 2
        d = d + 1

    while (a != b):
        if (a % 2 == 0): a = a / 2
        elif (b % 2 == 0): b = b / 2
        elif (a > b): a = (a - b) / 2
        else: b = (b - a) / 2

    g = a
    return g * (2 ** d)