def f(t, y):
    return 4 - t + (2 * y)

def approx_ode2(h, t0, y0, tn):
    t, y = t0, y0
    while abs(t - tn) > h/2.:
        y += h * ((0.5 * f(t, y)) + (0.5 * f(t + h, y)) + (h * f(t, y)))
        t += h
    
    return round(y, 3)