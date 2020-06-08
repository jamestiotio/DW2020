def position_velocity(v0, t):
    g = 9.81
    y0 = (v0 * t) - (0.5 * g * (t ** 2))
    y1 = v0 - (g * t)
    return (round(y0, 2), round(y1, 2))