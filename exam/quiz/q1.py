def range_float(start, end, n):
    if not isinstance(n, int):
        return 'Error'
    
    elif n <= 0:
        return 'Error'
    
    final_output = []
    counter = start
    step = (end - start) / (n - 1)
    
    while counter <= end:
        final_output.append(round(counter, 3))
        counter += step
        
    if final_output[-1] != end:
        return 'Error'
    
    return final_output