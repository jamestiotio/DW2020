def investment_val(amt, rate, years):
    return round(amt * ((1 + rate/1200) ** (years*12)), 2)