def multiplication_table(n):
    if n < 1:
        return None
    else:
        table = []
        for i in range(1, n+1):
            table.append([i * j for j in range(1, n+1)])
        
        return table