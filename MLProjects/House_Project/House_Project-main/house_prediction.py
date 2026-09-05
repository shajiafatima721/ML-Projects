import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset load
data = pd.read_csv("house_data.csv")

# City ko number me convert karo
data = pd.get_dummies(data, columns=["City"])

# Features aur Target
X = data.drop("Price", axis=1)
y = data["Price"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model banao
model = LinearRegression()

# Model train karo
model.fit(X_train, y_train)

print("Model Trained Successfully")

# User Input
area = int(input("Enter Area (sq ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
city = input("Enter City (Delhi, Ghaziabad, Kanpur, Lucknow, Noida): ")

# City columns
new_house = {
    "Area": [area],
    "Bedrooms": [bedrooms],
    "City_Delhi": [1 if city.lower() == "delhi" else 0],
    "City_Ghaziabad": [1 if city.lower() == "ghaziabad" else 0],
    "City_Kanpur": [1 if city.lower() == "kanpur" else 0],
    "City_Lucknow": [1 if city.lower() == "lucknow" else 0],
    "City_Noida": [1 if city.lower() == "noida" else 0]
}

new_house = pd.DataFrame(new_house)

predicted_price = model.predict(new_house)

print("\nPredicted House Price = ₹", round(predicted_price[0]))