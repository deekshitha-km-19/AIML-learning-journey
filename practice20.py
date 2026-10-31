import random

secret = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

if guess == secret:
    print("Correct! You won!")
else:
    print("Wrong! The number was", secret)


    a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" and b != 0:
    print(a / b)
else:
    print("Invalid operation")

    year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

    