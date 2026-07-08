# 🌸 Iris Flower Classification

## 📖 Overview

This project predicts the species of an Iris flower using Machine Learning. The application is built with **Streamlit**, containerized using **Docker**, and deployed on **Render**.

---

## 🌐 Live Demo

🚀 **Live Application:** https://iris-y2y0.onrender.com

---

## 📊 Dataset

- Dataset: `iris.csv`

---

## 📁 Project Files

- `iris.ipynb` – Data preprocessing, model training, and evaluation
- `iris.csv` – Dataset
- `iris_model.pkl` – Trained Machine Learning model
- `app.py` – Streamlit web application
- `requirements.txt` – Python dependencies
- `Dockerfile` – Docker configuration

---

## ⚙️ Workflow

- Data loading and inspection
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Train-test split
- Model training
- Model evaluation
- Prediction using the trained model

---

## 🤖 Models Used

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree

---

## 📈 Results

- Achieved **95%+ accuracy**
- Logistic Regression provided excellent classification performance

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker
- Render

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t harishprj/iris .
```

Run the Docker container:

```bash
docker run -p 8001:8501 harishprj/iris
```

---

## 👨‍💻 Author

**Harish Parajuli**
