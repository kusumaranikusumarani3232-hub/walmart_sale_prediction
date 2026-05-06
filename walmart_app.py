import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# LOAD MODEL
# ---------------------------
model = joblib.load("model.pkl")

# ---------------------------
# TITLE & DESCRIPTION
# ---------------------------
st.title("🛒 Walmart Sales Prediction App")

st.markdown("### About")
st.write("This app predicts Walmart weekly sales using Machine Learning (XGBoost) based on store, economic, and seasonal factors.")

# ---------------------------
# INPUT SECTION
# ---------------------------
st.header("📥 Input Features")

store = st.number_input("Store", value=10, min_value=1, step=1)
holiday = st.selectbox("Holiday Flag", [0, 1], index=0)
temp = st.number_input("Temperature", value=25.0)
fuel = st.number_input("Fuel Price", value=3.5)
cpi = st.number_input("CPI", value=210.0)
unemp = st.number_input("Unemployment", value=7.0)

year = st.number_input("Year", value=2011, min_value=2010, max_value=2025, step=1)
month = st.number_input("Month", value=11, min_value=1, max_value=12, step=1)
week = st.number_input("Week", value=45, min_value=1, max_value=52, step=1)

# ---------------------------
# PREDICTION SECTION
# ---------------------------
st.header("📊 Prediction Result")

if st.button("Predict"):
    if month > 12 or week > 52:
        st.error("Invalid Month or Week")
    else:
        data = np.array([[store, holiday, temp, fuel, cpi, unemp, year, month, week]])
        pred = model.predict(data)
        st.metric("Predicted Weekly Sales", f"{pred[0]:,.0f}")

# ---------------------------
# EDA SECTION
# ---------------------------
st.header("📈 Sales Trend Analysis")

try:
    df = pd.read_csv("walmart.csv")

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        trend = df.groupby("Date")["Weekly_Sales"].sum()

        fig, ax = plt.subplots()
        trend.plot(ax=ax)
        ax.set_title("Total Weekly Sales Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")

        st.pyplot(fig)

except:
    st.warning("Upload walmart.csv to view trend analysis")

# ---------------------------
# MODEL PERFORMANCE
# ---------------------------
st.header("📉 Model Performance")

st.write("XGBoost RMSE: 205,109")
st.write("Random Forest RMSE: 281,994")
st.write("Linear Regression RMSE: 510,406")
