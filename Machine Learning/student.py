import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('Student_dataset.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Performance prediction")

Age = st.number_input("Age :", min_value=16, max_value=71, value=16, step=1)
Income = st.number_input("Income :", min_value=1000, max_value=130000, value=1000)
Year_as_fn = st.number_input("Year_as_fn:", min_value=1, max_value=50, value=1, step=1 )
Number_of_Games = st.number_input("Number of Game :", min_value=1, max_value=100, value=1, step=1)
Team_Performance = st.number_input("Team_Performance :", min_value=0.0, max_value=10.0, value=0.0, step=0.5 )
Engagement_with_team = st.number_input("Engagement_with_team:", min_value=0, max_value=2, value=0, step=1 )




if st.button("Predict"):
    input_data = np.array([[Age, Income, Year_as_fn, Number_of_Games,Team_Performance,Engagement_with_team]])
    predicted_score = model.predict(input_data)[0]
    
    st.success(f"Predicted Score: {predicted_score} out of 1")