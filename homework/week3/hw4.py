from math import exp
import numpy as np

def f(t, y):
    return 3 + exp(-t) - (0.5 * y)

def approx_ode(h,t0,y0,tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    t, y = t0, y0
    for t in np.arange(t0, tn, h):
        y += h * f(t, y)

    return round(y, 3)