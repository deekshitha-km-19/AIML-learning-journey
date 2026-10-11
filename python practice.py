marks = [70, 80, 90, 60, 100]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
def square(num):
    return num * num

print(square(5))
print(square(8))
text = "AI ML AI Python ML AI"
words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
