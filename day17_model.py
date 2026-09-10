import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("RealEstate.csv")
print(df.head())
print(f"Total houses: {len(df)}")

X = df[["Sqft", "Bedrooms"]]
y = df["Price_Lakhs"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, pred):.2f}")

price = model.predict(pd.DataFrame([[1400, 3]], columns=["Sqft", "Bedrooms"]))
print(f"Predicted Price for 3BHK 1400sqft: {price[0]:.2f} Lakhs")