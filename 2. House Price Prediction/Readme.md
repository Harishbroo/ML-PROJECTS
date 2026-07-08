# 🏠 House Price Prediction

## 📖 Overview

This project predicts house prices using Machine Learning regression models based on housing data. The application is built with **Streamlit**, containerized using **Docker**, and deployed on **Render**.

---

## 📊 Dataset

- Source: Kaggle / Housing Dataset
- Dataset used: `dataset.csv`

---

## 📁 Project Files

- `house.ipynb` – Data preprocessing, EDA, feature engineering, model training, and evaluation
- `app.py` – Streamlit web application
- `model.pkl` – Trained Machine Learning model
- `requirements.txt` – Python dependencies
- `Dockerfile` – Docker configuration

---

## ⚙️ Workflow

- Data loading and inspection
- Handling missing values
- Exploratory Data Analysis (EDA)
- Feature engineering
- Feature selection and preprocessing
- Train-test split
- Model training and evaluation
- House price prediction using the trained model

---

## 🤖 Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## 📈 Results

- Evaluated using RMSE and MAE
- Random Forest achieved the best performance among the tested models

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
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
docker build -t harishprj/house-price .
```

Run the Docker container:

```bash
docker run -p 8001:8501 harishprj/house-price
```

---

## 🌐 Live Demo

**Render:** https://house-price-latest-6fru.onrender.com

---

## 👨‍💻 Author

**Harish Parajuli**
