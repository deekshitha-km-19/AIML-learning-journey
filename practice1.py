n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is largest")
else:
    print(b, "is largest")
    n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")