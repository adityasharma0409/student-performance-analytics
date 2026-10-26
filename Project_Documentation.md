# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details

**Project Title:** Student Performance Analytics System  
**Student Name:** Aditya Sharma  
**Course:** Python with AI  
**College:** Bharati Vidyapeeth College of Engineering (Deemed to be University), Pune, Maharashtra 
**Internship/Training Provider:** EWB Courses  
**Date:** 26/10/2026

## 2. Objective

The objective of this project is to build a Python-based system that reads student academic records and summarises performance. It calculates total and average marks, assigns grades, identifies pass/fail results, analyses subject-wise averages, and lists the top-performing students. The system helps present student data in a clear and understandable format.

## 3. Technologies Used

- **Python 3:** variables, data types, loops, conditions, functions, and program flow.
- **Pandas:** reads the CSV file into a DataFrame, displays records, and performs data analysis.
- **NumPy:** calculates numerical averages.
- **CSV:** stores the student dataset.
- **GitHub:** hosts the project files and documentation.

No machine learning model or additional framework is used.

## 4. Dataset Description

The project uses `students.csv`, containing 20 fictional student records. Each record contains:

- `student_id`: sample student identifier.
- `name`: student name.
- `department`: department.
- `math_marks`: Mathematics marks out of 100.
- `python_marks`: Python marks out of 100.
- `english_marks`: English marks out of 100.
- `attendance`: attendance percentage.

The dataset is small enough to understand and inspect, while containing enough records to demonstrate class and subject analysis.

## 5. Implementation

### Step 1: Load the dataset

The `load_dataset()` function uses `pandas.read_csv()` to load `students.csv` into a DataFrame. The program displays the number of rows and columns, the first five records, column names, and missing-value counts.

### Step 2: Calculate student results

The program uses a loop to visit each student record and collect the three subject marks. Reusable functions calculate the total, average, grade, and pass/fail result. The results are added to the DataFrame as new columns.

### Step 3: Calculate total and average

The total is the sum of the three subject marks. The average is calculated with `numpy.mean()` and displayed to two decimal places.

### Step 4: Assign grades

The program uses `if`, `elif`, and `else` conditions:

- Average of 85 or more: A
- Average of 70 or more but below 85: B
- Average of 55 or more but below 70: C
- Average of 35 or more but below 55: D
- Average below 35: F

### Step 5: Identify pass/fail students

A student passes only if every subject mark is at least 35. A loop checks the marks; if any mark is below 35, the student is marked Fail. This is the rule selected for this project and is not presented as an official college grading policy.

### Step 6: Analyse class performance

Pandas and NumPy operations calculate the number of students, overall class average, highest student average, lowest student average, and counts of passed and failed students.

### Step 7: Analyse subjects

The program calculates the mean for Mathematics, Python, and English. It then identifies the subject with the highest mean.

### Step 8: Identify top performers

The DataFrame is sorted by average marks in descending order. The first three records are displayed as the top three performers.

### Step 9: Validate the data

The program checks that required columns exist and that required fields do not contain missing values. If the CSV file or required columns are missing, it displays an understandable error message.

## 6. Key Features

1. Reads and displays student data.
2. Checks dataset structure and missing values.
3. Calculates total and average marks.
4. Assigns grades using explicit conditions.
5. Determines pass/fail results.
6. Summarises class performance.
7. Compares subject averages.
8. Lists the top three performers.
9. Uses reusable functions and loops.

## 7. Output / Screenshots

After running `python main.py`, capture screenshots of these sections:

1. Dataset loaded successfully, first five records, and dataset information.
2. Student-wise performance table.
3. Class performance and subject-wise averages.
4. Top three performers and the completion message.

Insert your actual screenshots here before final submission. Do not use invented screenshots or claim results that you have not run and checked.

## 8. Final Outcome

The project turns a CSV file containing student details, marks, and attendance into a readable performance report. It demonstrates basic Python programming, reusable functions, loops, conditions, NumPy numerical calculations, and Pandas DataFrame handling and analysis.

## 9. Challenges and Learning

Complete this section honestly after testing. Possible points to discuss, if they match your experience:

- Keeping CSV column names consistent with the Python program.
- Understanding how a DataFrame stores and displays tabular data.
- Writing functions so that calculations can be reused.
- Using conditions to apply grade and pass/fail rules.
- Checking for missing columns and missing values.
- Reading console output to verify the analysis.

Write about any actual error you encountered and how you fixed it.

## 10. GitHub Repository

**Repository URL:** [Paste your final public GitHub repository URL here]

Before submission, verify that the repository contains `main.py`, `functions.py`, `students.csv`, `README.md`, `Project_Documentation.md`, and `requirements.txt`. Confirm that the program runs successfully and that the repository link is the one submitted through the Google Form.
