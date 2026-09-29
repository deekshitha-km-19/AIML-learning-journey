import random

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))

    attempts = attempts + 1

    if guess == secret_number:
        print("🎉 Correct!")
        print("You found it in", attempts, "attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")