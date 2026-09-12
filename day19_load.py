import pickle

with open('house_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Model Loaded! Ready to predict")

mysore_1200 = [[1200, 0, 0, 1]]
price = model.predict(mysore_1200)
print(f"Mysore 1200 Sqft price: {price[0]:.2f} Lakh")

bangalore_1200 = [[1200, 1, 0, 0]]
price2 = model.predict(bangalore_1200)
print(f"Bangalore 1200 Sqft price: {price2[0]:.2f} Lakh")
mandya_1500 = [[1500, 0, 1, 0]]
price3 = model.predict(mandya_1500)
print(f"Mandya 1500 Sqft price: {price3[0]:.2f} Lakh")