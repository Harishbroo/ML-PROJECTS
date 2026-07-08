import streamlit as st
import pickle
import pandas as pd
import re

# Load trained pipeline
model = pickle.load(open("model.pkl", "rb"))

# ---------------------- TITLE ----------------------

st.title("🚢 Titanic Survival Prediction")

st.write(
    "Enter passenger details below to predict whether the passenger would survive."
)

# ---------------------- INPUTS ----------------------

col1, col2 = st.columns(2)

with col1:

    Pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    Sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

    Age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

    Fare = st.number_input(
        "Fare",
        min_value=0.0,
        value=32.20
    )

    Embarked = st.selectbox(
        "Embarked",
        ["S", "C", "Q"]
    )

with col2:

    SibSp = st.number_input(
        "Siblings / Spouse",
        min_value=0,
        value=0
    )

    Parch = st.number_input(
        "Parents / Children",
        min_value=0,
        value=0
    )

    Cabin = st.text_input(
        "Cabin (Optional)",
        ""
    )

    Name = st.text_input(
        "Passenger Name",
        "Braund, Mr. Owen Harris"
    )

# ---------------------- FEATURE ENGINEERING ----------------------

# Sex Encoding

if Sex == "Male":
    Sex = 0
else:
    Sex = 1

# Embarked Encoding

embarked_map = {
    "S": 0,
    "C": 1,
    "Q": 2
}

Embarked = embarked_map[Embarked]

# Deck Extraction

deck_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'T': 8
}

if Cabin.strip() == "":
    Deck = 0
else:
    Deck = deck_map.get(Cabin[0].upper(), 0)

# Family Features

FamilySize = SibSp + Parch + 1

IsAlone = 1 if FamilySize == 1 else 0

# Title Extraction

match = re.search(r'([A-Za-z]+)\.', Name)

if match:
    title = match.group(1)
else:
    title = ""

title_map = {
    'Mr': 1,
    'Miss': 2,
    'Mrs': 3,
    'Master': 4,
    'Dr': 5,
    'Rev': 6
}

Title = title_map.get(title, 0)

# Fare Per Person

FarePerPerson = Fare / FamilySize

# Age × Passenger Class

AgePclass = Age * Pclass

# ---------------------- PREDICTION ----------------------

if st.button("Predict Survival"):

    input_data = pd.DataFrame({

        "Pclass": [Pclass],
        "Sex": [Sex],
        "Age": [Age],
        "Embarked": [Embarked],
        "Deck": [Deck],
        "FamilySize": [FamilySize],
        "IsAlone": [IsAlone],
        "Title": [Title],
        "FarePerPerson": [FarePerPerson],
        "AgePclass": [AgePclass]

    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    if prediction == 1:

        st.success("🎉 Passenger is likely to Survive!")

        st.write(
            f"Confidence : {probability[1] * 100:.2f}%"
        )

    else:

        st.error("❌ Passenger is unlikely to Survive.")

        st.write(
            f"Confidence : {probability[0] * 100:.2f}%"
        )

# ---------------------- FOOTER ----------------------

st.write("---")

st.caption("Developed by Harish Parajuli")