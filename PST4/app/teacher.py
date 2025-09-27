import sys
sys.path.append('C:/Users/Admin/Desktop/FIT1056-Sem2-2025-new/PST4/app')
from user import User

class TeacherUser(User):
    """Represents a teacher."""
    # TODO: Implement the TeacherUser class, inheriting from User.
    # It should have an additional 'speciality' attribute in its __init__.
    def __init__(self, name, user_id = None, id = None, speciality = None, **kwargs):
        super().__init__(user_id or id, name)
        self.speciality = speciality or []

class Course:
    """Represents a single course offered by the school, linked to a teacher."""
    def __init__(self, name, instrument, enrolled_student_ids = None, teacher_id = None, course_id = None, id = None, lessons = None):
        self.id = course_id or id
        self.name = name
        self.instrument = instrument
        self.teacher_id = teacher_id or []
        # TODO: Initialize two empty lists: 'enrolled_student_ids' and 'lessons'.
        self.enrolled_student_ids = enrolled_student_ids or []
        self.lessons = lessons or [] # This will hold lesson dictionaries