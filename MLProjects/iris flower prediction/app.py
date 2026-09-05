
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_resource
def train_model():
    iris = load_iris()
    model = RandomForestClassifier()
    model.fit(iris.data, iris.target)
    return model, iris

model, iris = train_model()

st.title("🌼 Iris Flower Predictor")
st.write("Enter flower measurements below:")

sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

features = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button("Predict"):
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0]
    species = iris.target_names

    st.success(f"🌸 Prediction: **{species[prediction]}**")
    st.bar_chart(pd.Series(prob, index=species))
