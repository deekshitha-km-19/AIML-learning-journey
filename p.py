# Create student marks dataset
marks = [85, 90, 78, 92, 88]
print("Average marks:", sum(marks)/len(marks))
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Square:", arr**2)
print("Array * 2:", arr * 2)# How to calculate accuracy
correct = 85
total = 100
accuracy = (correct / total) * 100
print(f"Model Accuracy: {accuracy}%")

if accuracy > 80:
    print("Good Model!")
else:
    print("Need to improve model")
    text = "Hello!!! This is AIML Course... 123"

# Simple AI that predicts Pass/Fail
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))

if marks >= 40 and attendance >= 75:
    print("Prediction: PASS - You will clear AI exam")
else:
    print("Prediction: FAIL - Need more study")
