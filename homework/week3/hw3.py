def is_prime(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True

    return False