# 💎 Sonar Rock vs. Mine Prediction

## 📖 Overview

This project predicts whether an underwater object is a **Rock** or a **Mine** using Machine Learning. The application is built with **Streamlit**, containerized using **Docker**, and deployed on **Render**.

---

## 🌐 Live Demo

🚀 **Live Application:** https://sonar-latest.onrender.com

---

## 📊 Dataset

- Dataset: `sonardata.csv`
- Type: Binary Classification (Rock vs. Mine)
- Features: 60 continuous sonar frequency measurements

---

## 📁 Project Files

- `rockvsmine.ipynb` – Data preprocessing, model training, and evaluation
- `app.py` – Streamlit web application
- `sonar_model.pkl` – Trained Machine Learning model
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

## 🤖 Model Used

- Logistic Regression

---

## 📈 Results

- Successfully classified underwater objects as **Rock** or **Mine**
- Achieved high classification accuracy on the test dataset

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
docker build -t harishprj/sonar .
```

Run the Docker container:

```bash
docker run -p 8001:8501 harishprj/sonar
```

---

## 👨‍💻 Author

**Harish Parajuli**
