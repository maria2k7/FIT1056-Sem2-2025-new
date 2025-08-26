students = []
def register_students (name, age, instrument):
    student = {"name":name, "age":age, "instrument":instrument}
    students.append(student)
    return student

print (register_students ("Deez", 18, "Tuba"))

schedule = {
    "Monday 10 AM":"Piano Room A",
    "Monday 11 AM":"Guitar Room B"
}

def schedule_lesson (time, lesson):
    if time in schedule:
        print ("Unavailable")
    elif lesson not in schedule:
        print ("This class does not exist, please check again")
    else:
        schedule[time] = lesson
        print (f"Scheduled: {lesson} at {time}")

schedule_lesson ("10 AM", "Piano")

import hashlib

def store_student_secure(name, email):
    encoded = f"{name}:{email}".encode('utf-8')
    hashed = hashlib.sha256(encoded).hexdigest()
    print("Secured")
    print (hashed)

store_student_secure("Zarya", "ZKal1010@student.monash.edu")

import time

def sim_response():
    start = time.time()
    time.sleep(1.5)
    end = time.time()
    print ("Response time:", round (end - start, 2), "seconds")

sim_response()

