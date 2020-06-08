def longest_common_prefix(string1, string2):
    prefix = ""
    common_chars = list(zip(string1, string2))
    
    for char1, char2 in common_chars:
        if char1 == char2:
            prefix += char1
        else:
            break
    
    return prefix