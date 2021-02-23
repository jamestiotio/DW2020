def most_frequent(lst):
    main_dict = {}

    for number in set(lst):
        main_dict[number] = lst.count(number)

    max_val = max(main_dict, key=main_dict.get)

    return [x for x, v in main_dict.items() if v == main_dict[max_val]]