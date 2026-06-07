# 👥 Customer Churn Prediction

## 📖 Overview
This project predicts whether a customer will churn or not using machine learning. It includes data preprocessing, exploratory data analysis, feature engineering, and model training.

---

## 📊 Dataset
- dataset.csv (Customer churn dataset)

---

## 📁 Files
- churn.ipynb → Complete analysis and model training
- dataset.csv → Dataset used for training

---

## ⚙️ Workflow
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Encoding categorical variables
- Handling missing values
- Feature selection
- Train-test split
- Handling imbalance using SMOTE
- Model training and evaluation

---

## 📊 Exploratory Data Analysis (EDA)
- Churn distribution analysis
- Contract type vs churn
- Internet service vs churn
- Gender vs churn
- Senior citizen vs churn
- Monthly charges vs churn
- Tenure vs churn

---

## 🤖 Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier (Best Model)

---

## ⚖️ Imbalance Handling
- SMOTE used to balance dataset before training

---

## 📈 Results
- Random Forest performed best
- Evaluation metrics used:
  - Accuracy
  - Confusion Matrix
  - Classification Report

---

## 🚀 How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
jupyter notebook
