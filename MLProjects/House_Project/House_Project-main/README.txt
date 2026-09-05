# ?? House Price Prediction Using Machine Learning

A Machine Learning project that predicts house prices based on **area, number of bedrooms, and city**. The project uses **Linear Regression** for prediction and **Streamlit** to provide an interactive web application.

## ????? Author

**Shajia Fatima**

---

## ?? Project Overview

House prices can vary depending on several factors such as property size, number of bedrooms, and location.

This project builds a simple Machine Learning model that predicts the estimated price of a house based on:

* ?? Area (sq ft)
* ??? Number of Bedrooms
* ?? City

The model is trained using **Linear Regression** and the final prediction can be made through an interactive Streamlit application.

---

## ?? Objective

The main objective of this project is to:

* Build a basic Machine Learning regression model.
* Predict house prices from property features.
* Convert categorical city data into numerical features.
* Create an interactive prediction interface using Streamlit.
* Understand the complete workflow from data loading to model prediction.

---

## ??? Technologies Used

* **Python**
* **Pandas** — Data manipulation and preprocessing
* **Scikit-learn** — Machine Learning
* **Linear Regression** — Price prediction algorithm
* **Streamlit** — Interactive web application

---

## ?? Project Structure

```text
House-Price-Prediction/
¦
+-- house_prediction.py     # ML model training and prediction
+-- app.py                  # Streamlit web application
+-- house_data.csv          # Dataset
+-- README.md               # Project documentation
```

---

## ?? Machine Learning Workflow

The project follows these steps:

### 1. Load Dataset

The house dataset is loaded using Pandas:

```python
data = pd.read_csv("house_data.csv")
```

### 2. Data Preprocessing

The `City` column is categorical, so it is converted into numerical dummy variables using Pandas:

```python
data = pd.get_dummies(data, columns=["City"])
```

### 3. Define Features and Target

The input features are separated from the target variable:

```python
X = data.drop("Price", axis=1)
y = data["Price"]
```

The model uses the house features to predict **Price**.

### 4. Train-Test Split

The dataset is divided into training and testing sets:

```python
train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

This reserves 20% of the data for testing.

### 5. Train Linear Regression Model

A Linear Regression model is created and trained:

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

### 6. Make Predictions

After receiving the house details, the trained model predicts the estimated house price.

---

## ?? Streamlit Web Application

The project also includes a Streamlit interface where users can enter:

* Area in square feet
* Number of bedrooms
* City

The application provides five city options:

* Delhi
* Ghaziabad
* Kanpur
* Lucknow
* Noida

These options are implemented using a Streamlit select box.

After clicking **Predict Price**, the application displays the predicted house price.

---

## ?? How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 — Open the Project Folder

```bash
cd House-Price-Prediction
```

### Step 3 — Install Required Libraries

```bash
pip install pandas scikit-learn streamlit
```

### Step 4 — Run the Streamlit App

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## ?? Example Input

```text
Area: 1500 sq ft
Bedrooms: 3
City: Noida
```

The application will return an estimated house price based on the trained Linear Regression model.

---

## ?? Model

**Algorithm:** Linear Regression

**Target Variable:** `Price`

**Features:**

* `Area`
* `Bedrooms`
* City dummy variables

The project uses a straightforward regression approach to demonstrate how property features can be used to estimate house prices.

---

## ?? Limitations

This is a beginner-level Machine Learning project, so the prediction depends heavily on the dataset used for training.

The current model only considers:

* Area
* Bedrooms
* City

Real-world house prices can also depend on many additional factors such as property condition, neighborhood, floor, amenities, age of property, and market conditions.

Therefore, predictions should be treated as **estimates rather than actual market prices**.

---

## ?? Future Improvements

Possible improvements include:

* Add more property features.
* Perform detailed Exploratory Data Analysis (EDA).
* Handle missing values and outliers.
* Compare multiple regression algorithms.
* Evaluate the model using MAE, MSE, and R².
* Improve model accuracy through feature engineering.
* Add data visualizations to the Streamlit application.
* Save the trained model instead of training it every time the application starts.

---

## ?? Key Learning Outcomes

Through this project, I practiced:

* Loading datasets with Pandas
* Categorical data encoding
* Feature and target selection
* Train-test splitting
* Linear Regression
* Model training
* Making predictions
* Building an interactive Streamlit application
* Creating a complete end-to-end Machine Learning project

---

## ? Conclusion

This project demonstrates a complete basic Machine Learning workflow for house price prediction, starting from dataset loading and preprocessing to model training and deployment through an interactive Streamlit application.

**Developed by Shajia Fatima**
