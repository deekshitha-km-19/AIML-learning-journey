import pandas as pd
import numpy as np
np.random.seed(42)

size = np.random.randint(500, 4000, 1000)
bedrooms = np.random.randint(1, 6, 1000)
age = np.random.randint(1, 30, 1000)
price = size*300 + bedrooms*50000 - age*2000 + np.random.randint(-100000, 100000, 1000)

df = pd.DataFrame({'Size': size, 'Bedrooms': bedrooms, 'Age': age, 'Price': price})
df.to_csv("house_big.csv", index=False)
print("1000 rows created! Shape:", df.shape)
print(df.head())