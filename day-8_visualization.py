import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("house_price.csv")

# 1. Histogram - Price distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Price'], kde=True)
plt.title("House Price Distribution")
plt.savefig("price_hist.png")
plt.show()

# 2. Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()