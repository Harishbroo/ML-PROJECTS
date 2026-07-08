import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📞 Customer Churn Prediction")

st.write("Enter the customer details below.")

# Input fields
gender = st.number_input("Gender (0/1)", min_value=0, max_value=1, value=1)
senior = st.number_input("Senior Citizen (0/1)", min_value=0, max_value=1, value=0)
partner = st.number_input("Partner (0/1)", min_value=0, max_value=1, value=1)
dependents = st.number_input("Dependents (0/1)", min_value=0, max_value=1, value=0)
tenure = st.number_input("Tenure", min_value=0, value=12)
phone = st.number_input("Phone Service (0/1)", min_value=0, max_value=1, value=1)
multiple = st.number_input("Multiple Lines", min_value=0, value=0)
internet = st.number_input("Internet Service", min_value=0, value=0)
security = st.number_input("Online Security", min_value=0, value=0)
backup = st.number_input("Online Backup", min_value=0, value=0)
device = st.number_input("Device Protection", min_value=0, value=0)
support = st.number_input("Tech Support", min_value=0, value=0)
tv = st.number_input("Streaming TV", min_value=0, value=0)
movies = st.number_input("Streaming Movies", min_value=0, value=0)
contract = st.number_input("Contract", min_value=0, value=0)
paperless = st.number_input("Paperless Billing", min_value=0, max_value=1, value=1)
payment = st.number_input("Payment Method", min_value=0, value=0)
monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total = st.number_input("Total Charges", min_value=0.0, value=850.0)

if st.button("Predict"):

    features = np.array([[

        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone,
        multiple,
        internet,
        security,
        backup,
        device,
        support,
        tv,
        movies,
        contract,
        paperless,
        payment,
        monthly,
        total

    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is unlikely to churn.")