import pandas as pd
data = {
    'Name': ['Deekshitha', 'Aman', 'Priya'],
    'Marks': [85, 90, 78],
    'City': ['Bangalore', 'Delhi', 'Mumbai']
}

df = pd.DataFrame(data)
print(df)
print("\nAverage Marks:", df['Marks'].mean())