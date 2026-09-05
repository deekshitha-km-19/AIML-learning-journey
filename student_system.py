records = {}

def add_student(roll, name, cgpa):
    records[roll] = {"name": name, "cgpa": cgpa}
    print("Student added!")

def search_student(roll):
    if roll in records:
        print(records[roll])
    else:
        print("Not found")

# Test it
add_student(101, "Deekshitha", 8.5)
add_student(102, "Rahul", 8.0)
search_student(101)
print("All records:", records)