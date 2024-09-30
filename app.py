import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

model = load('model.joblib')

st.title('Waiter Tip Prediction App')

# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]

total_bill = st.number_input('Total Bill', min_value=0.0, max_value=100.0)
sex = st.selectbox('Sex', {"Female": 0, "Male": 1})
smoker = st.selectbox('Smoker', {"No": 0, "Yes": 1})
day = st.selectbox('Day', {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
time = st.selectbox('Time', {"Lunch": 0, "Dinner": 1})
size = st.number_input('Size', min_value=1, max_value=10)

sex_encoded = 0 if sex == "Female" else 1
smoker_encoded = 0 if smoker == "No" else 1
day_encoded = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}[day]
time_encoded = 0 if time == "Lunch" else 1

if st.button('Predict'):
    features = [[total_bill, sex_encoded, smoker_encoded, day_encoded, time_encoded, size]]
    prediction = model.predict(features)
    st.write(f'The predicted tip is: {prediction[0]:.2f}')
