def find_average(lst):
    list_of_average = []

    for item in lst:
        if not item:
            list_of_average.append(0.0)
        else:
            list_of_average.append(sum(item)/len(item))

    flattened_list = [item for sublist in lst for item in sublist]
    overall_average = sum(flattened_list)/len(flattened_list)

    return (list_of_average, overall_average)