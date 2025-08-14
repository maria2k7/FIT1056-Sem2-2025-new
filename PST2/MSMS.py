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
def add_student(name):
    """Adds a student dictionary to the data store."""
    student_id = app_data["next_student_id"]
    new_student = {"id": student_id, "name": name, "attendance" : []}
    app_data['students'].append(new_student)
    app_data['next_student_id'] += 1
    print(f"Core: Student '{name}' added.")
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

#ID Card printing & Receptionist features
def check_in(student_id, course_id, timestamp=None):
    """Records a student's attendance for a course."""
    if timestamp is None:
        timestamp = datetime.datetime.now().isoformat()
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    app_data['attendance'].append(check_in_record)
    print(f"Receptionist: Student {student_id} checked into {course_id}.")

def print_student_card(student_id):
    """Creates a text file badge for a student."""
    student_to_print = None
    for s in app_data['students']:
        if s['id'] == student_id:
            student_to_print = s
            break
    
    if student_to_print != None:
        filename = f"{student_id}_card.txt"
        with open(filename, 'w') as f:
            f.write("========================\n")
            f.write(f"  MUSIC SCHOOL ID BADGE\n")
            f.write("========================\n")
            f.write(f"ID: {student_to_print['id']}\n")
            f.write(f"Name: {student_to_print['name']}\n")
            f.write(f"Enrolled In: {', '.join(student_to_print.get('enrolled_in', []))}\n")
        print(f"Printed student card to {filename}.")
    else:
        print(f"Error: Could not print card, student {student_id} not found.")

# Main function, for real this time
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            sid = str(input("Please enter your student id: "))
            cid = str(input("Please enter your course id: "))
            check_in(sid,cid)
            made_change = True
        elif choice == '2':
            sid = str(input("Please enter your student id: "))
            print_student_card(sid)
            print ("Your student ID card is ready to be used.")
            pass 
        elif choice == '3':
            tid = str(input("Please enter your teacher id: "))
            news = str(input("Please enter the details you want to updapte: "))
            update_teacher(tid, news)
            made_change = True
        elif choice == '4':
            sid = str(input("Please enter your student id: "))
            remove_student(sid)
            made_change = True
        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change == True:
            save_data(msms.json) # Save the data immediately after any change.

    save_data(msms.json) # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()







