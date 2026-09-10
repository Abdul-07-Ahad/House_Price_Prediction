import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/house.csv")

# Features
X = df[["Area", "Bedrooms", "Age"]]

# Target
y = df["Price"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save model
with open("models/house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")

print("Model saved as models/house_model.pkl")
