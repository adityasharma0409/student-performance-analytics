import numpy as np


def calculate_total(marks):
    """Return the total of a student's subject marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of a student's subject marks."""
    return float(np.mean(marks))


def assign_grade(average):
    """Assign a grade using the project's documented grading rule."""
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "F"


def get_result(marks):
    """A student passes only when every subject mark is at least 35."""
    for mark in marks:
        if mark < 35:
            return "Fail"
    return "Pass"


def get_subject_averages(dataframe, subject_columns):
    """Calculate the average mark for each subject using NumPy."""
    averages = {}
    for subject in subject_columns:
        averages[subject] = float(np.mean(dataframe[subject].to_numpy()))
    return averages
