
import random

print("🎮 WELCOME TO NUMBER GUESSING GAME!")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("\nEnter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You WIN!")
        break

    elif guess > secret_number:
        print("📉 Too high! Try a smaller number.")

    else:
        print("📈 Too low! Try a bigger number.")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("😢 Game Over!")
    print("The correct number was:", secret_number)

print("Thanks for playing!")
