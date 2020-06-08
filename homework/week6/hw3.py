def get_base_counts2(dna):
    if not all(char.isalpha() for char in dna):
        return "The input DNA string is invalid"
    elif not all(char.isupper() for char in dna):
        return "The input DNA string is invalid"
    
    total = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for letter in dna:
        if letter in total.keys():
            total[letter] += 1
    
    return total