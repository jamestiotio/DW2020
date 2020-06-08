def letter_grade(mark):
    if mark < 0 or mark > 100:
        return None
    elif mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    elif mark < 60:
        return 'E'