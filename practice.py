name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college: ")
cgpa = float(input("Enter your CGPA: "))

print("\n----- Student Details -----")
print("Name:", name)
print("Age:", age)
print("College:", college)
print("CGPA:", cgpa)

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total:", total)
print("Average:", average)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("My name is", name)
print("My age is", age)

marks = [80, 75, 90, 85, 70]

total = sum(marks)
average = total / len(marks)

print("Total =", total)
print("Average =", average)
numbers = [10, 25, 7, 42, 18]

print("Largest =", max(numbers))
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area =", area)