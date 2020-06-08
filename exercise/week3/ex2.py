def my_reverse(lst):
    new_lst = []
    count = len(lst) - 1
    
    while count >= 0:
        new_lst.append(lst[count])
        count -= 1
        
    return new_lst