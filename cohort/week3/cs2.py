def minmax_in_list(ls):
    if not ls:
        return (None, None)
    else:
        smallest = ls[0]
        for i in ls:
            if smallest > i:
                smallest = i

        biggest = ls[0]
        for j in ls:
            if biggest < j:
                biggest = j
        
        return (smallest, biggest)