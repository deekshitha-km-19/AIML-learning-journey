import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CREATE SAMPLE DATA (so no file needed) ---
data = {
    'Location': ['Mysore', 'Bangalore', 'Mysore', 'Bangalore', 'Mysore', 'Hyderabad', 'Bangalore', 'Hyderabad', 'Mysore', 'Bangalore'],
    'Price': [50, 120, 45, 150, 60, 90, 130, 85, 55, 110],
    'Area': [1000, 1200, 800, 1500, 1100, 1000, 1300, 900, 950, 1250]
}
df = pd.DataFrame(data)

# --- 1. SORTING ---
print("Sorted by Price:")
print(df.sort_values(by='Price', ascending=True))

print("\nTop 5 Expensive:")
df_top5 = df.sort_values(by='Price', ascending=False).head(5)
print(df_top5)

# --- 2. VISUALIZATION ---

# a) Bar - Avg Price by Location
plt.figure()
df.groupby('Location')['Price'].mean().sort_values().plot(kind='barh', color='skyblue')
plt.title('Average Price by Location (Sorted)')
plt.xlabel('Average Price')
plt.show()

# b) Histogram - Price Distribution
plt.figure()
plt.hist(df['Price'], bins=10, color='skyblue', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# c) Boxplot - Outliers
plt.figure()
sns.boxplot(x=df['Price'])
plt.title('Boxplot - Price')
plt.show()

# d) Scatter - Price vs Area
plt.figure()
plt.scatter(df['Area'], df['Price'])
plt.title('Price vs Area')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()

# e) Top 5 bar
plt.figure()
sns.barplot(x='Price', y='Location', data=df_top5, palette='viridis')
plt.title('Top 5 Most Expensive Properties')
plt.show()

print("Day 15 Completed!")