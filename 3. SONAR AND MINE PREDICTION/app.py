import streamlit as st
import numpy as np
import pickle

with open("sonar_model.pkl","rb") as f:
    model = pickle.load(f)

st.title("Rock or Mine Prediction")

user_input = st.text_area(
    "Enter 60 values separated by commas"
)

if st.button("Predict"):

    values = list(map(float, user_input.split(",")))

    prediction = model.predict([values])

    if prediction[0] == "R":
        st.success("Rock")
    else:
        st.error("Mine")