num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

    num = int(input("Enter a number: "))
count = len(str(abs(num)))

print("Number of digits:", count)

num = int(input("Enter a number: "))
total = 0

for digit in str(abs(num)):
    total += int(digit)

print("Sum of digits:", total)