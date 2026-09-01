import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('house_price.csv')

print("--- DAY 7 EDA ---")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDescription:\n", df.describe())

price_col = df.columns[-1] 
plt.hist(df[price_col], bins=20)
plt.title(f'Distribution of {price_col}')
plt.show()