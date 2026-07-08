import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt


# Load model

model = pickle.load(open("kmeans_model.pkl","rb"))


st.title("🛒 Customer Segmentation using KMeans")


st.write(
"""
This app segments customers into groups based on:
- Annual Income
- Spending Score
"""
)


# User input

income = st.number_input(
    "Annual Income (k$)",
    min_value=1,
    max_value=200,
    value=50
)


score = st.number_input(
    "Spending Score (1-100)",
    min_value=1,
    max_value=100,
    value=50
)


if st.button("Predict Cluster"):

    data = np.array([[income,score]])


    cluster = model.predict(data)[0]


    st.success(
        f"Customer belongs to Cluster {cluster+1}"
    )


    # show position

    X = model.cluster_centers_


    fig,ax = plt.subplots(figsize=(7,5))


    ax.scatter(
        X[:,0],
        X[:,1],
        s=200,
        marker="X",
        label="Centroids"
    )


    ax.scatter(
        income,
        score,
        s=100,
        label="New Customer"
    )


    ax.set_xlabel("Annual Income")
    ax.set_ylabel("Spending Score")
    ax.set_title("Customer Cluster")


    ax.legend()


    st.pyplot(fig)