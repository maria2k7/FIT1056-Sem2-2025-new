# main.py - The View Layer
import sys
sys.path.append('C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST3/app')
from schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    manager._load_data()
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # TODO: Call a method on the manager to get the day's lessons and print them.
    pass

def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    student = manager.find_student_by_id(student_id)
    current_course = manager.find_course_by_id(from_course_id)
    new_course = manager.find_course_by_id(to_course_id)
    if not student or not current_course or not new_course:
        print("Something went wrong, please double check the deatails entered.")
    else:
        if from_course_id in student.enrolled_course_ids:
            student.enrolled_course_ids.remove(from_course_id)
            student.enrolled_course_ids.append(to_course_id)
            current_course.enrolled_student_ids.remove(student_id)
            new_course.enrolled_student_ids.append(student_id)
            print(f"Success: Student {student.name} has switched from {current_course.name} to {new_course.name}!")
        else:
            print("This student has not enrolled into this course, please check again.")

    pass

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager() # Create ONE instance of the application brain.
    
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        # TODO: Create a menu for the new PST3 functions.
        # Get user input and call the appropriate view function, passing 'manager' to it.
        choice = input("Enter choice: ")
        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            front_desk_daily_roster(manager, day)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            from_course_id = input("Enter current course ID: ")
            to_course_id = input("Enter new course ID: ")
            switch_course(manager, student_id, from_course_id, to_course_id)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            find_student = manager.find_student_by_id(student_id)
            if find_student == True:
                print("Student found.")
            else:
                print("Student does not exist. Perhaps you are searching for a wrong person?")
        elif choice == "4":
            course_id = input("Enter course ID: ")
            find_course = manager.find_course_by_id(course_id)
            if find_course == True:
                print("Course found.")
            else:
                print("Course does not exist. At least, not yet.")
        elif choice.lower() == 'q':
            break
        
if __name__ == "__main__":
    main()