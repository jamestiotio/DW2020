def reverse(string):
    new_string = ""
    for char in range(1, len(string) + 1):
        new_string += string[-char]

    return new_string