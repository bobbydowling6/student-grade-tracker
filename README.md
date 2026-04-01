# student-grade-tracker
What You're Building

A Python script that reads student grade data from a CSV, calculates averages, assigns letter grades, and writes a formatted summary report.

Setup

No external packages needed — this uses only Python's built-in csv module.

# Make sure you're in the project folder
cd project/starter/

# Run the script
python3 grade_tracker.py
Files

starter/
├── data/
│   └── students.csv      ← input data (15 students, some missing grades)
├── grade_tracker.py      ← your work goes here (implement the 5 functions)
├── requirements.txt      ← empty (no external packages)
└── README.md
Your Task

Open grade_tracker.py and implement the 5 stub functions:

Function	What it does
load_students(filepath)	Reads CSV, returns list of dicts
calculate_average(grades)	Averages grade values, skips missing
get_letter_grade(average)	Converts number → A/B/C/D/F
generate_report(students)	Builds class summary dict
write_report(report, filepath)	Writes formatted report to file
Do NOT modify main() — it orchestrates your functions and shows you what the expected output looks like.

# Expected Output

When all functions are implemented, running python3 grade_tracker.py should print something like:

=== Student Grade Tracker ===

Loaded 10 students from students.csv

--- Individual Results ---
Alice Johnson      | Avg: 90.5 | Grade: A
Bob Smith          | Avg: 80.3 | Grade: B
Charlie Brown      | Avg: 68.8 | Grade: D
Diana Prince       | Avg: 95.5 | Grade: A
Eve Davis          | Avg: 49.0 | Grade: F
Frank Wilson       | Avg: 83.8 | Grade: B
Grace Lee          | Avg: 91.8 | Grade: A
Henry Adams        | Avg: 71.3 | Grade: C
Isabel Cruz        | Avg: 87.3 | Grade: B
Jack Turner        | Avg: 53.8 | Grade: F

--- Class Statistics ---
Class Average: 77.1
Highest: Diana Prince (95.5)
Lowest: Eve Davis (49.0)

Subject Averages:
  Math:    76.7
  Science: 77.9
  English: 76.8
  History: 77.3

Add a new student? (yes/no): no

Report written to grade_report.txt
Summary written to students_summary.csv
Done!