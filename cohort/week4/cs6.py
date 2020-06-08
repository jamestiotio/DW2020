def get_base_counts(dna):
    total = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for letter in dna:
        if letter not in total.keys():
            return 'The input DNA string is invalid'
        else:
            total[letter] += 1
    
    return total