import pickle

# Load trained model
with open("models/house_model.pkl", "rb") as file:
    model = pickle.load(file)

# Take input from the user
area = float(input("Enter Area: "))
bedrooms = int(input("Enter Bedrooms: "))
age = int(input("Enter Age: "))

prediction = model.predict([[area, bedrooms, age]])

print(f"\nPredicted Price: {prediction[0]:,.2f}")
