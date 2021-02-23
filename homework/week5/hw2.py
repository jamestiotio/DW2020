# NB: the following line imports the 'display_calendar', 'lear_year', etc. functions
# (see the problem sheet PDF)
# DO NOT delete hw2_others.pyc from Vocareum :-)
from hw2_others import *

# You should ONLY submit the 'display_calendar_modified' function

def initial_month_day(year):
    output = []
    jan1 = day_of_week_jan1(year)
    prev_first_day = jan1
    num_days = []

    output.append(jan1)

    for month in range(1, 12):
        num_days.append(num_days_in_month(month, leap_year(year)))

    for each_month in num_days:
        prev_first_day = (prev_first_day + each_month) % 7
        output.append(prev_first_day)

    return output

def display_calendar_modified(year, month):
    if month is None:
        return display_calendar(year)
    
    else:
        main_output = ""
        month_sublist = construct_cal_month(month, initial_month_day(year)[month - 1], num_days_in_month(month, leap_year(year)))
        
        main_output += month_sublist[0] + "\n"
        main_output += "  S  M  T  W  T  F  S\n"
        
        for week in month_sublist[1:]:
            if week == month_sublist[-1]:
                main_output += week
            else:
                main_output += week + "\n"
            
        return main_output