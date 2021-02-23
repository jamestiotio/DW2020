def compound_value_months(amt, rate, months):
    total = 0
    n = 1
    while n <= months:
        total = (amt + total) * (1 + (rate / 12))
        n += 1

    return round(total, 2)