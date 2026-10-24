import numpy as np

def calculate_total(marks):
    return np.sum(marks)

def calculate_average(marks):
    return np.mean(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def get_result(avg, attendance):
    if avg >= 40 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"