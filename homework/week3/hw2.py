def get_even_list(ls):
    new_ls = []
    for i in ls:
        if i % 2 == 0:
            new_ls.append(i)

    return new_ls