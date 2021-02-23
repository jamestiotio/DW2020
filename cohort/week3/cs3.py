def is_palindrome(num):
    normal=num
    reverse=0
    while (num > 0):
        dig = num % 10
        reverse = reverse * 10 + dig
        num = num // 10
    return bool(normal == reverse)