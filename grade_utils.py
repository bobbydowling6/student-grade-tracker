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