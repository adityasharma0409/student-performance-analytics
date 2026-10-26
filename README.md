# Student Performance Analytics System

A beginner-friendly Python data-analysis project for the **Python with AI** internship assignment. It reads student records from a CSV file and analyses marks using Python, NumPy, and Pandas.

## Features

- Reads student records from `students.csv` into a Pandas DataFrame.
- Shows the dataset, its shape, columns, and missing-value counts.
- Calculates each student's total marks and average marks.
- Assigns grades using a clearly documented grading rule.
- Determines pass/fail status using a subject-wise condition.
- Reports the class average, highest average, lowest average, and pass/fail counts.
- Calculates subject-wise averages and identifies the best-performing subject.
- Lists the top three performers.

## Concepts used

Only the concepts requested by the assignment are used: variables, data types, loops, conditions, functions, NumPy, Pandas, and basic data analysis. No machine learning model is used.

## Requirements

- Python 3
- NumPy
- Pandas

## Setup and run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python main.py
   ```

Keep `main.py`, `functions.py`, and `students.csv` in the same folder.

## Dataset

The sample dataset contains 20 fictional student records. Columns:

- `student_id`: unique sample ID
- `name`: student name
- `department`: department name
- `math_marks`, `python_marks`, `english_marks`: marks out of 100
- `attendance`: attendance percentage

The data is fictional and is included for demonstration.

## Rules used in this project

### Grade rule (based on average marks)

| Average | Grade |
|---:|:---|
| 85–100 | A |
| 70–84.99 | B |
| 55–69.99 | C |
| 35–54.99 | D |
| Below 35 | F |

### Pass/fail rule

A student passes only if **each of the three subject marks is at least 35**. If any subject mark is below 35, the result is Fail.

Attendance is displayed as student information; it does not change the pass/fail result because the assignment does not specify an attendance threshold.

## Project files

- `main.py` — loads the dataset and displays the analysis.
- `functions.py` — reusable calculation, grade, result, and subject-average functions.
- `students.csv` — sample dataset.
- `Project_Documentation.md` — detailed project report.
- `requirements.txt` — required Python packages.
- `.gitignore` — excludes common temporary files.

## Expected output sections

When the program runs, it displays the first five records, basic dataset information, student-wise totals/averages/grades/results, class performance, subject-wise averages, and the top three performers. Exact numeric results are calculated from the CSV file at runtime.

