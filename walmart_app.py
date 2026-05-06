import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Walmart Sales Prediction")

store = st.number_input("Store")
holiday = st.selectbox("Holiday Flag", [0,1])
temp = st.number_input("Temperature")
fuel = st.number_input("Fuel Price")
cpi = st.number_input("CPI")
unemp = st.number_input("Unemployment")

if st.button("Predict"):
    data = np.array([[store, holiday, temp, fuel, cpi, unemp]])
    pred = model.predict(data)
    st.success(f"Predicted Sales: {pred[0]}")