import pandas as pd
df = pd.read_csv('house_prices.csv')
print("1. First 5 rows:")
print(df.head())

print("\n2. Shape (rows, cols):")
print(df.shape)

print("\n3. Column names:")
print(df.columns.tolist())

print("\n4. Average Price:")

if 'Price' in df.columns:
    print(df['Price'].mean())
else:
    print(df.iloc[:, 1].mean(), "- (2nd column mean)")

print("\n5. Missing values:")
print(df.isnull().sum())