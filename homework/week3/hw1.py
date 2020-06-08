def temp_convert(choice, temp):
    if choice == "C":
        return (temp - 32) * (5/9)
    elif choice == "F":
        return (temp * (9/5)) + 32
    else:
        return None