def transpose_matrix(matrix):
    # return [list(i) for i in zip(*matrix)]
    new_matrix = [[] for i in range(len(matrix[0]))]
    for row in matrix:
        for index, element in enumerate(row):
            new_matrix[index].append(element)

    return new_matrix