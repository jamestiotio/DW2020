# NB: you do not need to submit the 'get_data' function

def extract_values(values):
    if len(values.split(" ")) == 2:
        return (int(values.split(" ")[0]), int(values.split(" ")[1]))

def calc_ratios(values):
    if values[1] == 0:
        return None
    else:
        return values[0] / values[1]