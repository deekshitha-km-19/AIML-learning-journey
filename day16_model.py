import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_price.csv")
print("Total houses:", len(df))

df['BHK'] = pd.to_numeric(df['Size'], errors='coerce')
df = df[["BHK", "Price"]].dropna()

X = df[["BHK"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

new_house = [[3]]
price = model.predict(new_house)
print(f"Predicted Price for 3 BHK: {price[0]} Lakhs")
print("Day 16 Done! 🎉")