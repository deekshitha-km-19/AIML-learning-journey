class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "C"

    def display(self):
        return f"Name: {self.name}, marks: {self.marks}, Grade: {self.get_grade()}"

# Take input from user
name1 = input("Enter student1 name: ")
marks1 = int(input("Enter student1 marks: "))

name2 = input("Enter student2 name: ")
marks2 = int(input("Enter student2 marks: "))

student1 = Student(name1, marks1)
student2 = Student(name2, marks2)

print(student1.display())
print(student2.display())

if student1.marks > student2.marks:
    print(f"Topper is {student1.name}!")
elif student2.marks > student1.marks:
    print(f"Topper is {student2.name}!")
else:
    print("Both are toppers! Tie!")