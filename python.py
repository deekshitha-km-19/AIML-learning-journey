from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [2, 2], [3, 3], [5, 5], [6, 6]]
y = [0, 0, 0, 1, 1]  

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

prediction = model.predict([[5, 4]])
print("Prediction:", prediction[0])
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("In 5 years, you will be", age + 5)