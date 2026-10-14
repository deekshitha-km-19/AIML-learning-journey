numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)

numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)

foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")

student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)

student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)

student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")

students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]

student_marks = {}

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercased_cities = [city.upper() for city in cities]
print(uppercased_cities)
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

sentence = "I love coding in Python"
words = sentence.split()
print(words)

data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)

matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   