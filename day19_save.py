import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    'Location': ['Bangalore','Bangalore','Mysore','Mysore','Mandya','Mandya'],
    'Sqft': [1000,1400,1000,1400,1000,1400],
    'Price': [55,78,28,40,18,25]
}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['Location'])
X = df_encoded.drop('Price', axis=1)
y = df_encoded['Price']

model = LinearRegression()
model.fit(X, y)

with open('house_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model Saved! Check files -> house_model.pkl created")
print("Columns:", list(X.columns))