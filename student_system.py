
students = {}

def add_student(roll, name, cgpa):
    students[roll] = {"name": name, "cgpa": cgpa}
    print(f"Added {name}")

def search_student(roll):
    if roll in students:
        print(f"Found: {students[roll]}")
    else:
        print("Roll", roll, "not found!")

def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f"Roll {roll} deleted!")
    else:
        print("Roll", roll, "not found!")

# --- now call them AFTER defining ---
add_student(101, "Deekshitha", 8.5)
add_student(102, "Anjali", 9.0)
search_student(101)
delete_student(102)
search_student(102)