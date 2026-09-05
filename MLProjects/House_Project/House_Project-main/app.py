import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Predict house prices using Machine Learning.")

# Load Dataset
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(BASE_DIR, "house_data.csv"))

# Convert City to Dummy Variables
data = pd.get_dummies(data, columns=["City"])

# Features and Target
X = data.drop("Price", axis=1)
y = data["Price"]

# Train Model
model = LinearRegression()
model.fit(X, y)

st.header("Enter House Details")

area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

city = st.selectbox(
    "Select City",
    ["Delhi", "Ghaziabad", "Kanpur", "Lucknow", "Noida"]
)

if st.button("Predict Price"):

    new_house = {
        "Area": [area],
        "Bedrooms": [bedrooms],
        "City_Delhi": [1 if city == "Delhi" else 0],
        "City_Ghaziabad": [1 if city == "Ghaziabad" else 0],
        "City_Kanpur": [1 if city == "Kanpur" else 0],
        "City_Lucknow": [1 if city == "Lucknow" else 0],
        "City_Noida": [1 if city == "Noida" else 0]
    }

    new_house = pd.DataFrame(new_house)
    new_house = new_house.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(new_house)

    st.success(f"🏡 Predicted House Price: ₹ {round(prediction[0]):,}")

st.markdown("---")
st.write("Developed by Shajia")
