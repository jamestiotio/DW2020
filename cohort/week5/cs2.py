import math

def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    x = 1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)
    return x % 7

def num_days_in_month(month_num, leap_year):
    if month_num == 2:
        if leap_year:
            return 29
        else:
            return 28
    
    elif month_num in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    
    elif month_num in [4, 6, 9, 11]:
        return 30

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    output = []
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    output.append(months.get(month_num))
    
    week_list = []
    
    initial_jump = first_day_of_month
    number_of_weeks = -((num_days_in_month + initial_jump) // -7)  # Ceiling division
    
    week = 1
    day_count = 1
    
    for week in range(1, number_of_weeks + 1):
        if week == 1:
            jumpcut = "   " * initial_jump
            rest_of_first_week = ""
            
            while day_count <= (7 - initial_jump):
                rest_of_first_week += "  {}".format(day_count)
                day_count += 1
            
            jumpcut += rest_of_first_week
            week_list.append(jumpcut)
        
        elif week == number_of_weeks:
            final_week = ""
            
            while day_count <= num_days_in_month:
                final_week += " {}".format(day_count) 
                day_count += 1
            
            week_list.append(final_week)
        
        else:
            subsequent_week = ""
            
            while day_count <= num_days_in_month:
                
                if day_count <= (week * 7 - initial_jump):
                    
                    # Digit checker
                    if int(math.log10(day_count)) + 1 == 1:
                        subsequent_week += "  {}".format(day_count)
                    elif int(math.log10(day_count)) + 1 == 2:
                        subsequent_week += " {}".format(day_count)
                        
                    day_count += 1
                    
                else:
                    week_list.append(subsequent_week)
                    subsequent_week = ""
                    break
    
    output.extend(week_list)
    
    return output

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

def construct_cal_year(year):
    output = []
    output.append(int(year))
    
    first_days = initial_month_day(year)
    
    months = []
    
    for month in range(1, 13):
        month_sublist = construct_cal_month(month, first_days[month - 1], num_days_in_month(month, leap_year(year)))
            
        months.append(month_sublist)
    
    output.extend(months)
    
    return output

def display_calendar(year):
    year_list = construct_cal_year(year)
    year_list.remove(year_list[0])
    
    main_output = ""
    
    for month in year_list:
        main_output += month[0] + "\n"
        main_output += "  S  M  T  W  T  F  S\n"
        
        for week in month[1:]:
            if month[0] == "December" and week == month[-1]:
                main_output += week
            else:
                main_output += week + "\n"
            
        if month[0] == "December":
            pass
        else:
            main_output += "\n"
    
    return main_output