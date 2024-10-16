import pickle
import pandas as pd
import streamlit as st 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error



with open("dataset.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Salary Predict")

iq_level = st.number_input("Enter",min_value=0.0,max_value=50.0,value=1.0,step=0.1)


if st.button("Predict"):
    prediction = model.predict([[iq_level]])
    st.success(f"Predicted salary: ${prediction[0]:,.2}")