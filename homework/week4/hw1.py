def f_to_c(f):
    return round((f - 32) * (5 / 9), 1)

def f_to_c_approx(f):
    return round((f - 30) / 2, 1)

def get_conversion_table_a():
    final_result = []
    for temp in list(range(0, 110, 10)):
        final_result.append([temp, f_to_c(temp), f_to_c_approx(temp)])
        
    return final_result

def get_conversion_table_b():
    final_result = [[] for i in range(3)]
    for temp in list(range(0, 110, 10)):
        final_result[0].append(temp)
        final_result[1].append(f_to_c(temp))
        final_result[2].append(f_to_c_approx(temp))
        
    return final_result