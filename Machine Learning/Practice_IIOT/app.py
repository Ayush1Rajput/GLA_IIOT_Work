import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('dataset.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Exam_Score Prediction App")

hours_studied = st.number_input("Hours Studied:", min_value=0.0, max_value=24.0, value=1.0, step=0.5)
practice_tests = st.number_input("Number of Practice Tests Taken:", min_value=0, max_value=20, value=1)
attendance_rate = st.number_input("Attendance:", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
sleep_hours = st.number_input("Average Sleep Hours:", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

if st.button("Predict"):
    input_data = np.array([[hours_studied, practice_tests, attendance_rate, sleep_hours]])
    predicted_score = model.predict(input_data)[0]
    
    st.success(f"Predicted Score: {predicted_score:.2f} out of 100")