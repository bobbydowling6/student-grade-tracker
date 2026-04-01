import csv

# This function loads student data from a CSV file and returns a list of dictionaries, where each dictionary represents a student with their details.
def load_students(filepath: str) -> list:
    students = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students
    # todo filenotfounderror
pass

def calculate_student_average(student: dict) -> float:
    # This function calculates the average grade for a student based on their grades in different subjects.
    grades = []
    for subject, value in student.items():
        if subject.lower() == 'name':
            continue
        try:
            grades.append(float(value))
        except (TypeError, ValueError):
            continue

    average = sum(grades) / len(grades) if grades else 0.0
    return average

def get_letter_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
def get_class_statistics(students: list) -> dict:
    # This function calculates class statistics such as average grade, highest grade, and lowest grade.
    if not students:
        return {
            'average': 0.0,
            'highest': 0.0,
            'lowest': 0.0,
            'highest_student': None,
            'lowest_student': None,
        }
    
    student_averages = [
        (calculate_student_average(student), student)
        for student in students
    ]
    class_average = sum(avg for avg, _ in student_averages) / len(student_averages)
    highest_grade, highest_student = max(student_averages, key=lambda item: item[0])
    lowest_grade, lowest_student = min(student_averages, key=lambda item: item[0])
    
    return {
        'average': class_average,
        'highest': highest_grade,
        'lowest': lowest_grade,
        'highest_student': highest_student,
        'lowest_student': lowest_student,
    }

print("=== Student Grade Tracker ===")
print()
print(f"Loaded {len(load_students('students.csv'))} students from students.csv file.")
print()
print("=== Individual Results ===")
print()
students = load_students('students.csv')
for student in students:
    average = calculate_student_average(student)
    letter_grade = get_letter_grade(average)
    print(f"{student['name']} | Average Grade = {average:.2f} | Letter Grade = {letter_grade}")
print()
stats = get_class_statistics(students)
print(f"Class Average: {stats['average']:.2f}")
if stats['highest_student']:
    print(f"Highest Grade: {stats['highest_student']['name']} {stats['highest']:.2f}")
else:
    print(f"Highest Grade: {stats['highest']:.1f}")
if stats['lowest_student']:
    print(f"Lowest Grade: {stats['lowest_student']['name']} {stats['lowest']:.2f}")
else:
    print(f"Lowest Grade: {stats['lowest']:.1f}")