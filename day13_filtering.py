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

expensive_blr = df[(df['Price'] > 5000000) & (df['Location'] == 'Bangalore')]
print("\nExpensive Bangalore (>50L):")
print(expensive_blr)

chennai_or_small = df[(df['Location'] == 'Chennai') | (df['Area'] < 1000)]
print("\nChennai OR Small:")
print(chennai_or_small)

print(f"\nTotal Bangalore houses: {len(blr)}")