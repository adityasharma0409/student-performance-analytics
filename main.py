import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    get_result,
    get_subject_averages,
)

DATA_FILE = "students.csv"
SUBJECT_COLUMNS = ["math_marks", "python_marks", "english_marks"]


def load_dataset(file_name):
    """Load the CSV file into a Pandas DataFrame."""
    dataframe = pd.read_csv(file_name)
    return dataframe


def add_student_results(dataframe):
    """Calculate total, average, grade, and pass/fail for every student."""
    totals = []
    averages = []
    grades = []
    results = []

    for index in range(len(dataframe)):
        marks = []
        for subject in SUBJECT_COLUMNS:
            marks.append(int(dataframe.loc[index, subject]))

        total = calculate_total(marks)
        average = calculate_average(marks)
        grade = assign_grade(average)
        result = get_result(marks)

        totals.append(total)
        averages.append(round(average, 2))
        grades.append(grade)
        results.append(result)

    dataframe["total_marks"] = totals
    dataframe["average_marks"] = averages
    dataframe["grade"] = grades
    dataframe["result"] = results
    return dataframe


def display_student_summary(dataframe):
    print("\n" + "=" * 72)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print("\nSTUDENT-WISE PERFORMANCE")
    columns = [
        "student_id", "name", "department", "total_marks",
        "average_marks", "grade", "result", "attendance"
    ]
    print(dataframe[columns].to_string(index=False))


def display_class_analysis(dataframe):
    print("\nCLASS PERFORMANCE")
    print("-" * 72)
    print("Number of students:", len(dataframe))
    print("Overall class average:", round(float(np.mean(dataframe["average_marks"])), 2))
    print("Highest student average:", round(float(dataframe["average_marks"].max()), 2))
    print("Lowest student average:", round(float(dataframe["average_marks"].min()), 2))
    print("Students passed:", int((dataframe["result"] == "Pass").sum()))
    print("Students failed:", int((dataframe["result"] == "Fail").sum()))


def display_subject_analysis(dataframe):
    print("\nSUBJECT-WISE AVERAGE")
    print("-" * 72)
    subject_averages = get_subject_averages(dataframe, SUBJECT_COLUMNS)
    for subject, average in subject_averages.items():
        readable_name = subject.replace("_marks", "").replace("_", " ").title()
        print(readable_name + " average:", round(average, 2))

    best_subject = max(subject_averages, key=subject_averages.get)
    print("Best-performing subject:", best_subject.replace("_marks", "").title())


def display_top_performers(dataframe):
    print("\nTOP 3 PERFORMERS")
    print("-" * 72)
    top_students = dataframe.sort_values(
        by="average_marks", ascending=False
    ).head(3)
    print(top_students[["student_id", "name", "average_marks", "grade"]].to_string(index=False))


def main():
    try:
        students = load_dataset(DATA_FILE)
    except FileNotFoundError:
        print("Error: students.csv was not found.")
        print("Keep main.py, functions.py, and students.csv in the same folder.")
        return

    required_columns = ["student_id", "name", "department"] + SUBJECT_COLUMNS + ["attendance"]
    missing_columns = []
    for column in required_columns:
        if column not in students.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Error: required columns are missing:", ", ".join(missing_columns))
        return

    print("Dataset loaded successfully.")
    print("Dataset shape (rows, columns):", students.shape)
    print("\nFirst five records:")
    print(students.head().to_string(index=False))
    print("\nBasic dataset information:")
    print("Columns:", ", ".join(students.columns))
    print("Missing values by column:")
    print(students.isnull().sum().to_string())

    if students[required_columns].isnull().any().any():
        print("\nError: the dataset contains missing values. Please correct students.csv.")
        return

    students = add_student_results(students)
    display_student_summary(students)
    display_class_analysis(students)
    display_subject_analysis(students)
    display_top_performers(students)

    print("\n" + "=" * 72)
    print("Analysis completed successfully.")
    print("=" * 72)


if __name__ == "__main__":
    main()
