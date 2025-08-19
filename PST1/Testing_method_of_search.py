name_to_find = input("Enter patient name: ")
found = False
for name, log in patients:
    if name.lower() == name_to_find.lower():
        print(f"{name}'s log says: {log}")
        found = True
        break
    if not found:
        print("Patient not found in the system.")

"""
I used it as a refference, 
and to experiment if it can work as a good search method to adapt to MSMS. 
Credits to Dr. Charith's slides for week 2's workshop 
"""