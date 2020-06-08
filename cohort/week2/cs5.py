def describe_bmi(bmi):
    if bmi < 18.5:
        return "nutritional deficiency"
    elif 18.5 <= bmi < 23:
        return "low risk"
    elif 23 <= bmi < 27.5:
        return "moderate risk"
    elif bmi >= 27.5:
        return "high risk"