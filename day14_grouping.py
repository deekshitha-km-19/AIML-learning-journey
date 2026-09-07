import pandas as pd
df = pd.read_csv('RealEstate.csv')

print("Data Loaded!")
print(df.head())

avg_price = df.groupby('Location')['Price_Lakhs'].mean()
print("\n--- Task 1: Average Price per City ---")
print(avg_price)

house_count = df.groupby('Location').size()
print("\n--- Task 2: House Count per City ---")
print(house_count)

avg_both = df.groupby('Location').agg({
    'Price_Lakhs': 'mean',
    'Sqft': 'mean'
})
print("\n--- Task 3: Avg Price & Sqft per City ---")
print(avg_both)