import pandas as pd

df = pd.read_csv('house_prices.csv')

costly = df[df['Price'] > 6000000]
print("Costly houses (>60L):")
print(costly)

small_houses = df[df['Area'] < 1000]
print("\nSmall houses (<1000 sqft):")
print(small_houses)


blr = df[df['Location'] == 'Bangalore']
print("\nOnly Bangalore:")
print(blr)