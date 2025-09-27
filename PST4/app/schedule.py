import sys
import json
import datetime
sys.path.append('C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST4/app')
from student import StudentUser
from teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST4/data/msms.json"):
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
                self.students = [StudentUser(**s) for s in data.get("students",[])]
                self.teachers = [TeacherUser(**s) for s in data.get("teachers",[])]
                self.courses = [Course(**c) for c in data.get("courses",[])]
                # TODO: Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
                self.attendance_log = data.get("attendance", [])
                print ("The data has been retrieved successfully")
                return data
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
            return {"students": [], "teachers": [], "courses": [], "attendance": []}    
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
                return student
        return None
    def find_course_by_id(self, course_id):
        for course in self.courses:
            if getattr(course, 'course_id', None) == course_id:
                return course
        return None 
    def register_new_student(self, student_name, course_name):
        self._load_data()
        new_id = max ([s.id for s in self.students], default=0) + 1
        enrolled_course = next((c for c in self.courses if c.name == course_name), None)
        if not enrolled_course:
            raise ValueError (f"Course {course_name} does not exist.")
        new_student = StudentUser(id=new_id, name=student_name, enrolled_course_ids=[enrolled_course.id])
        self.students. append(new_student)
        self._save_data()
        print("done!")
        return new_student
    # # TODO: Also implement find_student_by_id and find_course_by_id helper methods.