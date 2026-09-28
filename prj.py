def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    return total, average


name = input("Enter your name: ")

marks = []

for i in range(3):
    mark = float(input("Enter marks: "))
    marks.append(mark)


total, average = calculate_result(marks)


if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"


if average >= 40:
    result = "PASS"
else:
    result = "FAIL"


print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)