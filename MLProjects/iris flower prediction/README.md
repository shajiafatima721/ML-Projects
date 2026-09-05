# 🌼 Iris Flower Predictor

A Machine Learning web application that predicts the species of an Iris flower based on its sepal and petal measurements.

The application is built using **Python, Scikit-learn, Pandas, and Streamlit**. A **Random Forest Classifier** is trained on the built-in Iris dataset and used to predict the flower species.

## 👩‍💻 Author

**Shajia Fatima**

---

## 📌 Project Overview

The Iris Flower Predictor is a simple Machine Learning classification project designed to predict the species of an Iris flower from four measurements:

* 🌿 Sepal Length
* 🌿 Sepal Width
* 🌸 Petal Length
* 🌸 Petal Width

The user enters these measurements through an interactive Streamlit interface and clicks the **Predict** button to get the predicted Iris species.

---

## 🎯 Objective

The main objectives of this project are:

* Build a Machine Learning classification model.
* Use the Iris dataset for flower species classification.
* Apply Random Forest Classification.
* Create an interactive web interface using Streamlit.
* Display prediction probabilities for each Iris species.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Random Forest Classifier**
* **Streamlit**

---

## 📊 Dataset

This project uses the **Iris dataset** provided directly by Scikit-learn.

The dataset contains measurements of Iris flowers and three different species:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

The dataset is loaded using Scikit-learn's `load_iris()` function.

### Features

| Feature      | Description               |
| ------------ | ------------------------- |
| Sepal Length | Length of the sepal in cm |
| Sepal Width  | Width of the sepal in cm  |
| Petal Length | Length of the petal in cm |
| Petal Width  | Width of the petal in cm  |

### Target

**Iris Species**

---

## 🤖 Machine Learning Model

### Random Forest Classifier

The project uses a **Random Forest Classifier** to classify Iris flowers into their respective species.

The model is trained using all four flower measurements:

```python
model = RandomForestClassifier()
model.fit(iris.data, iris.target)
```

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to make predictions.

---

## 🔄 How the Application Works

### Step 1 — Enter Flower Measurements

The Streamlit application asks the user to enter:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

These four values are collected through Streamlit number input fields.

### Step 2 — Create Features

The entered values are combined into a feature array:

```python
features = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]
```

### Step 3 — Make Prediction

When the user clicks **Predict**, the trained Random Forest model predicts the flower species.

### Step 4 — Display Result

The predicted species is displayed in the application along with a probability chart for the possible species.

---

## 🌐 Streamlit Application

The project provides an interactive Streamlit interface called:

**🌼 Iris Flower Predictor**

Users can enter flower measurements and instantly receive a prediction.

The application also displays a bar chart showing the model's prediction probabilities for each species.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Iris-Flower-Predictor
```

### 3. Install Dependencies

Create a `requirements.txt` file containing:

```text
streamlit
pandas
scikit-learn
```

Then install them:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
Iris-Flower-Predictor/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 💡 Example

### Input

```text
Sepal Length: 5.1 cm
Sepal Width: 3.5 cm
Petal Length: 1.4 cm
Petal Width: 0.2 cm
```

### Output

```text
🌸 Prediction: setosa
```

The application also displays the prediction probability for each Iris species.

---

## 📈 Key Learning Outcomes

Through this project, I learned and practiced:

* Machine Learning classification
* Random Forest algorithm
* Working with the Scikit-learn Iris dataset
* Feature preparation
* Model prediction
* Prediction probabilities
* Streamlit application development
* Deploying Machine Learning models as web applications

---

## 🔮 Future Improvements

Possible improvements include:

* Add model accuracy and evaluation metrics.
* Add confusion matrix visualization.
* Add feature importance visualization.
* Compare Random Forest with other classification algorithms.
* Improve the Streamlit UI.
* Add interactive data visualizations.

---

## ⭐ Conclusion

The Iris Flower Predictor demonstrates a complete beginner-friendly Machine Learning classification workflow, from loading the dataset and training a Random Forest model to making predictions through an interactive Streamlit web application.

**Developed by Shajia Fatima**
