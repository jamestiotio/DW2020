import math

def minutes_to_years_days(minutes):
    years = math.floor(minutes/525600)
    days  = math.floor((minutes - (years * 525600))/1440)
    return (years, days)