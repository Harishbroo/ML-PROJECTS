import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# ------------------ PAGE TITLE ------------------
st.title("🏠 California House Price Prediction")

st.markdown("""
Predict California house prices using an **XGBoost Regressor**
trained on the **California Housing Dataset**.
""")

# ------------------ SIDEBAR ------------------
st.sidebar.title("ℹ️ About")

st.sidebar.info("""
**Model:** XGBoost Regressor

**Dataset:** California Housing Dataset

**Developed by:**
Harish Parajuli
""")

# ------------------ INPUTS ------------------
st.subheader("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input("Median Income", value=8.30)
    HouseAge = st.number_input("House Age", value=41.0)
    AveRooms = st.number_input("Average Rooms", value=4.00)
    AveBedrms = st.number_input("Average Bedrooms", value=1.02)

with col2:
    Population = st.number_input("Population", value=322.0)
    AveOccup = st.number_input("Average Occupancy", value=2.55)
    Latitude = st.number_input("Latitude", value=37.88)
    Longitude = st.number_input("Longitude", value=-122.23)

# ------------------ PREDICTION ------------------
if st.button("🔮 Predict Price"):

    input_data = np.array([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]])

    prediction = model.predict(input_data)

    price = prediction[0] * 100000

    st.success(f"🏡 Estimated House Price: ${price:,.2f}")

    st.balloons()

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Developed by Harish Parajuli")