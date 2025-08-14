import json
import datetime

DATA_FILE = "msms.json"
app_data = {}

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


