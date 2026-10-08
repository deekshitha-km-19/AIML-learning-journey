print("================================")
print("       🎮 PYTHON QUIZ GAME")
print("================================")

name = input("Enter your name: ")

score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. <!--"],
        "answer": "C"
    }
]

print("\nWelcome", name, "! Let's start the quiz.\n")

for i, q in enumerate(questions, 1):

    print("Question", i)
    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", q["answer"], "\n")

print("================================")
print("          RESULT")
print("================================")

print("Player:", name)
print("Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage == 100:
    print("🏆 Excellent! Perfect score!")
elif percentage >= 75:
    print("🥳 Great job!")
elif percentage >= 50:
    print("👍 Good attempt!")
else:
    print("📚 Keep practicing!")

print("================================")