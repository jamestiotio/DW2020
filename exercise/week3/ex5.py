def simpsons_rule(f, n, a, b):
    h = (b - a) / n
    
    sum1 = 0
    for i in range(1, int(n/2)):
        sum1 += f(a + (2 * i * h))
    
    sum2 = 0
    for j in range(1, int(n/2 + 1)):
        sum2 += f(a + (2 * j - 1) * h)
    
    approx = (h / 3) * (f(a) + (2 * sum1) + (4 * sum2) + f(b))
    return approx