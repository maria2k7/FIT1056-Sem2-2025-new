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
class person:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        self.salary = 30000
        self.total_ppl = 0
        self.total_ppl += 1
class stoodent(person):
    def show_total():
        print("Total monkeys created:", person.total_ppl)
    def introduce(self):
        print(f"Hi, I'm {self.name} and I play the {self. subject}")

s1 = stoodent("Maya", "11", "Violin")
s2 = stoodent("Hikari", "17", "Piano")
s1.introduce()
s2.introduce()
class teacher(person):
    def introduce(self):
        print(f"Hi, I'm {self.name} and I teach the {self.subject}")
    def set_salary(self, value):
        if 30000 <= value <= 150000:
            self.salary = value
            print ("Aight bro")
        else:
            print("Nuh uh, what is ts?")
    def get_salary(self):
        return print(self.salary)
t1 = teacher("Dr.Ligma", "28", "Horn")
t1.set_salary(10000000)
t1.get_salary()
t1.introduce()
ppl = [stoodent("Hikari","17","piano"), stoodent("Maya","11","violin"),teacher("Dr.Ligma","28","Horn")]
for people in ppl:
    people.introduce()

stoodent.show_total()

