def diff(p):
    result = {}
    for order, coeff in p.items():
        if order == 0:
            pass
        else:
            result[order - 1] = order * coeff

    return result