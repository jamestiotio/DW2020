def get_fundamental_constants(f):
    final_dict = {}
    lines = f.readlines()
    
    for line in lines[2:]:
        actual_line = " ".join(line.split())
        final_dict[actual_line.split(" ")[0]] = float(actual_line.split(" ")[1])
        
    return final_dict