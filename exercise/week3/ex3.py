import math

def approx_pi(n):
    temp_sum = 0
    for k in range(n+1):
        temp_sum += ((math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k))))
    
    return 1 / ((2 * math.sqrt(2) * temp_sum) / 9801)