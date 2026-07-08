# 👥 Customer Churn Prediction

## 📖 Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning. It features an end-to-end classification pipeline that handles class imbalance using **SMOTE**, compares multiple classification models, optimizes the best model using **GridSearchCV**, and deploys the final model through a **Streamlit** web application. The application is containerized using **Docker** and deployed on **Render**.

---

## 🌐 Live Demo

🚀 **Live Application:** https://customer-churn-85qa.onrender.com

---

## 📊 Dataset

- Dataset: `dataset.csv`
- Problem Type: Binary Classification
- Domain: Telecom Customer Churn Prediction

---

## 📁 Project Files

- `churn.ipynb` – Data preprocessing, EDA, model training, evaluation, and hyperparameter tuning
- `dataset.csv` – Telecom customer dataset
- `churn_model.pkl` – Optimized Random Forest model
- `app.py` – Streamlit web application
- `requirements.txt` – Python dependencies
- `Dockerfile` – Docker configuration

---

## ⚙️ Workflow

- Data loading and inspection
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Encoding categorical variables
- Handling missing values
- Train-test split with stratification
- Handling class imbalance using **SMOTE**
- Model training and evaluation
- Cross-validation
- Hyperparameter tuning using **GridSearchCV**
- Model serialization using **Pickle**
- Customer churn prediction

---

## 📊 Exploratory Data Analysis (EDA) Key Insights

- Month-to-month contract customers have the highest churn rate.
- Customers using Fiber Optic internet are more likely to churn.
- Customers with shorter tenure and higher monthly charges are at greater risk of leaving.
- Gender has little impact on customer churn.

---

## 🤖 Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier (Best Model)

---

## ⚖️ Imbalance Handling

- SMOTE (Synthetic Minority Over-sampling Technique)

---

## 📈 Results

- Average Cross-Validation Accuracy: **83.8%**
- Best model selected using **GridSearchCV**
- Important features:
  - MonthlyCharges
  - TotalCharges
  - Contract
  - Tenure
- Evaluated using:
  - Accuracy Score
  - Confusion Matrix
  - Precision
  - Recall
  - F1-Score

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
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
docker build -t harishprj/customer-churn .
```

Run the Docker container:

```bash
docker run -p 8001:8501 harishprj/customer-churn
```

---

## 👨‍💻 Author

**Harish Parajuli**
