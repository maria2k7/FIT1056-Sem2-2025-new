import json
import datetime
import sys
sys.path.append('C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST4/app')
from student import StudentUser
from teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST3/data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        # TODO: Initialize the new attendance_log attribute as an empty list.
        self.attendance_log = []
        # ... (next_id counters) ...
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # TODO: Load students, teachers, and courses as before.
                # ...
                self.students = data.get("students", [])
                self.teachers = data.get("teachers", [])
                self.courses = data.get("courses", [])
                # TODO: Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
                self.attendance_log = data.get("attendance", [])
                print ("The data has been retrieved successfully")
                print(self.courses)
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # TODO: Create a 'data_to_save' dictionary.
        data_to_save = {
            "students": [s.__dict__ for s in self.students],
            "teachers": [t.__dict__ for t in self.teachers],
            "courses": [c.__dict__ for c in self.courses],
            # TODO: Add the attendance_log to the dictionary to be saved.
            # Since it's already a list of dicts, no conversion is needed.
            "attendance": self.attendance_log,
            # ... (next_id counters) ...
        }
        # TODO: Write 'data_to_save' to the JSON file.
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)
    def check_in(self, student_id, course_id):
        """Records a student's attendance for a course after validation."""
        # This implementation remains the same, but it will now function correctly.
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
    
        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False
        
        timestamp = datetime.datetime.now().isoformat()
        check_in_record = {"student_id": student_id, "course_id": course_id, "timestamp": timestamp}
    
        # This line will now work without causing an AttributeError.
        self.attendance_log.append(check_in_record)
        self._save_data() # This will now correctly save the attendance log.
        print(f"Success: Student {student.name} checked into {course.name}.")
        return True

    def find_student_by_id(self, user_id):
        for student in self.students:
            if getattr(student, 'user_id', None) == user_id:
                print (student)
                return True
        return None
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if getattr(course, 'course_id', None) == course_id:
                print (course)
                return True
        return None 
    def register(self, student, course):
        data = self.load_data()
        if "students" not in data:
            data ["students"] = []
        new_id = max ([s["id"]for s in data["students"]], default=0) + 1
        enrolled_course_ids = self.get(course_name)
        student = {
            "id" = new_id
            "name" = student_name
            "enrolled_course_ids" = enrolled_course_ids
        }
        data ["students"]. append(student)
        self.save_data(data)
        print("done!")
    # # TODO: Also implement find_student_by_id and find_course_by_id helper methods.