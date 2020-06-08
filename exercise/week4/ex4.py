import random
import math

def pi_approx_monte_carlo(n):
    raindrop = 0
    for _ in range(n):
        x2 = random.random() ** 2
        y2 = random.random() ** 2
        if math.sqrt(x2 + y2) < 1:
            raindrop += 1
        
    pi = 4 * (raindrop / n)
    
    return round(pi, 2)