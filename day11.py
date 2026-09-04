student = {
    "name": "Deekshitha",
    "course": "CSE",
    "cgpa": 8.5,
    "skills": ["Python", "ML"]
}

print(student["name"])
print(student.get("cgpa"))

# Add new
student["goal"] = "AI Engineer"

# Loop
for key, value in student.items():
    print(f"{key} : {value}")

# Practice: Student marks dictionary
marks = {"Python": 90, "Maths": 85, "DSA": 88}
print("Average:", sum(marks.values()) / len(marks))