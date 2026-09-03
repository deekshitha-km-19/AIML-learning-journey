import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("house_big.csv")

# 1. Scatter + Regression - Size vs Price
plt.figure(figsize=(8,5))
sns.regplot(x='Size', y='Price', data=df, scatter_kws={'alpha':0.5})
plt.title("Size vs Price - With Trend Line")
plt.savefig("day9_scatter.png")
plt.show()

# 2. Boxplot - Price by Bedrooms
plt.figure(figsize=(8,5))
sns.boxplot(x='Bedrooms', y='Price', data=df)
plt.title("Price Distribution by Bedrooms")
plt.savefig("day9_boxplot.png")
plt.show()

# 3. PRO Heatmap - Now it will show colors!
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap - Big Data")
plt.savefig("day9_heatmap.png")
plt.show()