import json
import datetime

DATA_FILE = "msms.json"
app_data = {}
#core json load and save data functions section
def load_data(path=DATA_FILE):
    global app_data
    try:
        with open (path, "r") as f:
            app_data = json.load(f)
            print ("The data has been retrieved successfully")
    except FileNotFoundError:
        print ("Data file does not exist, initialize with default structure")
        app_data = {
            "students": [],
            "teachers": [],
            "attendance": [],
            "next_student_id": 1,
            "next_teacher_id": 1
        }
def save_data(path = DATA_FILE):
    with open (path, "r") as f:
        json.dump(app_data, f, indent = 4)
    print ("The data has been saved successfully")
#CRUD for both teachers and students
def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    teacher_id = app_data["next_teacher_id"]
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    app_data['teachers'].append(new_teacher)
    app_data['next_teacher_id'] += 1
    print(f"Core: Teacher '{name}' added.")
def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    for teacher in app_data['teachers']:
        if teacher['id'] == teacher_id:
            teacher.update(fields)
            print(f"Teacher {teacher_id} updated.")
        else:
            print(f"Error: Teacher with ID {teacher_id} not found.")
def remove_teacher(teacher_id):
    if teacher['id'] == teacher_id:
        app_data['teachers'].remove(app_data['teachers'][teacher_id - 1])
    else:
        print ("This teacher does not exist in the reccords")
def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields."""
    for student in app_data['student']:
        if student['id'] == student_id:
            student.update(fields)
            print(f"Student {student_id} updated.")
        else:
            print(f"Error: Student with ID {student_id} not found.")
def remove_student(student_id):
    if student['id'] == student_id:
        app_data['students'].remove(app_data['students'][students_id - 1])
    else:
        print ("This student does not exist in the reccords")







