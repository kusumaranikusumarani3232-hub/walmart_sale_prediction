# 🛒 Walmart Sales Prediction App

## 📌 Project Overview

This project focuses on predicting Walmart weekly sales using Machine Learning techniques.
It combines **Exploratory Data Analysis (EDA)**, **ML models**, and a **Streamlit web app** to deliver real-time predictions based on input features.

---

## 🎯 Objective

* Analyze sales trends and patterns
* Build predictive models for weekly sales
* Deploy an interactive web application

---

## 📊 Dataset

* Walmart Sales Dataset
* Features include:

  * Store
  * Holiday Flag
  * Temperature
  * Fuel Price
  * CPI
  * Unemployment
  * Date (converted into Year, Month, Week)

---

## 🔍 Exploratory Data Analysis (EDA)

* Sales trends over time
* Store-wise performance
* Holiday vs non-holiday impact
* Correlation analysis

---

## 🤖 Machine Learning Models Used

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor (Best Model ✅)

---

## 📈 Model Performance

| Model             | RMSE      |
| ----------------- | --------- |
| Linear Regression | 510,406   |
| Random Forest     | 281,994   |
| XGBoost           | 205,109 ✅ |

---

## 🚀 Deployment

The model is deployed using **Streamlit**.

### Features of the App:

* User input for prediction
* Real-time sales prediction
* Sales trend visualization
* Model performance display

---

## 🖥️ How to Run the Project

### 1. Clone repository

```
git clone https://github.com/your-username/walmart-sales-prediction.git
cd walmart-sales-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit app

```
streamlit run walmart_app.py
```

---

## 📂 Project Structure

```
Walmart_Project/
├── walmart_app.py
├── model.pkl
├── walmart.csv
├── README.md
```

---

## 💡 Key Learnings

* End-to-end ML pipeline development
* Feature engineering (Date → Year, Month, Week)
* Model comparison & evaluation
* Streamlit deployment

---

## 📸 Output Screenshot

(Add your app screenshot here)

---

## 🔗 Future Improvements

* Add Deep Learning (LSTM) forecasting
* Improve UI design
* Integrate real-time data

---

## 👤 Author

Kusumarani

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
