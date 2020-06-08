def uncompress(string):
    output = ""
    counter = 0
    
    while counter < len(string):
        output += string[counter+1] * int(string[counter])
        counter += 2
    
    return output