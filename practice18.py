
import random

print("=" * 40)
print("       PYTHON CODE QUEST")
print("=" * 40)
print("Welcome, Future AI/ML Engineer!")
print("Answer questions and earn XP.")
print()

xp = 0
lives = 3

questions = [
    {
        "question": "1. What is the output of print(2 + 3)?",
        "options": ["A. 23", "B. 5", "C. 6"],
        "answer": "B",
        "hint": "The + operator adds numbers."
    },
    {
        "question": "2. Which keyword checks a condition?",
        "options": ["A. if", "B. repeat", "C. show"],
        "answer": "A",
        "hint": "It starts a conditional statement."
    },
    {
        "question": "3. What is the output of 7 % 2?",
        "options": ["A. 3", "B. 0", "C. 1"],
        "answer": "C",
        "hint": "% gives the remainder."
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. str", "B. bool", "C. list"],
        "answer": "B",
        "hint": "Its name starts with 'b'."
    },
    {
        "question": "5. Which library is commonly used for arrays in AI/ML?",
        "options": ["A. NumPy", "B. Turtle", "C. Random"],
        "answer": "A",
        "hint": "It is widely used for numerical computing."
    }
]

random.shuffle(questions)

for q in questions:
    if lives == 0:
        break

    print("\n" + "-" * 40)
    print(q["question"])

    for option in q["options"]:
        print(option)

    print("Type H for a hint.")
    answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == "H":
        print("Hint:", q["hint"])
        answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == q["answer"]:
        print("Correct! +10 XP")
        xp += 10
    else:
        print("Incorrect!")
        print("Correct answer:", q["answer"])
        lives -= 1
        print("Lives remaining:", lives)

    print("Current XP:", xp)

print("\n" + "=" * 40)
print("          GAME OVER")
print("=" * 40)
print("Final XP:", xp, "/ 50")

if xp == 50:
    print("Amazing! Python Champion!")
elif xp >= 30:
    print("Great job! Keep practising.")
else:
    print("Keep learning. Try again!")

print("Your AI/ML journey starts here!")
