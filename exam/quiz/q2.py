def is_prime(n):
    # Corner cases 
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip  
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

def prime_factors(num):
    if not isinstance(num, int):
        return None

    elif num <= 1:
        return None

    elif is_prime(num):
        return None

    smaller_factor = 0
    larger_factor = 0

    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            if is_prime(i):
                smaller_factor = i
                if is_prime(num / i):
                    larger_factor = num / i
                    break

                else:
                    return None

    return (smaller_factor, larger_factor)