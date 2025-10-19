import sys
sys.path.append('C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST5/app')
from user import User

class StudentUser(User):
    """Represents a student, inheriting from the base User class."""
    def __init__(self, name, user_id = None, id = None, enrolled_course_ids = None, **kwargs):
        # TODO: Call the parent class's __init__ method using super().
        super().__init__(user_id or id, name)
        # TODO: Initialize an empty list called 'enrolled_course_ids' to store the IDs of courses.
        self.enrolled_course_ids = enrolled_course_ids or []