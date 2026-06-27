# 👥 Customer Churn Prediction

## 📖 Overview
This project predicts whether a customer will churn or not using machine learning. It features an end-to-end classification pipeline that handles severe data imbalance, evaluates multiple algorithms, and saves the optimized model for deployment.

---

## 📊 Dataset
- `dataset.csv` (Telecom customer churn dataset)

---

## 📁 Files
- `churn.ipynb` → Complete data analysis, SMOTE resampling, and model training
- `dataset.csv` → Raw dataset used for training
- `churn_model.pkl` → The final optimized Random Forest model saved via Pickle

---

## ⚙️ Workflow
- Data cleaning (dropping `customerID`, converting `TotalCharges` to numeric)
- Exploratory Data Analysis (EDA) with visualization
- Encoding categorical variables using `LabelEncoder` and `get_dummies`
- Handling missing values by filling `TotalCharges` NaNs with 0
- Train-test split with stratification (`stratify=y`)
- Handling class imbalance using **SMOTE**
- Model training, evaluation, and 5-fold cross-validation
- Hyperparameter tuning using **GridSearchCV**
- Model serialization with `pickle`

---

## 📊 Exploratory Data Analysis (EDA) Key Insights
- **Contract Type:** Month-to-month contract customers show the highest churn rates.
- **Internet Service:** Fiber optic users churn significantly more than DSL or non-internet users.
- **Financials & Loyalty:** Shorter tenure and higher monthly charges strongly correlate with a customer leaving.
- **Gender:** Does not show a significant impact on customer churn behavior.

---

## 🤖 Models Used
- Logistic Regression
- Decision Tree Classifier
- **Random Forest Classifier** (Best Model - Tuned via GridSearchCV & saved)

---

## ⚖️ Imbalance Handling
- **SMOTE** (Synthetic Minority Over-sampling Technique) was applied exclusively to the training set to prevent the classifiers from being biased toward non-churning customers.

---

## 📈 Results & Evaluation
- The Random Forest model achieved a strong average cross-validation score of **83.8%**.
- **Top Predictors:** `MonthlyCharges`, `TotalCharges`, `Contract`, and `tenure` were identified as the most crucial features impacting the model's predictions.
- Full evaluation was verified using:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-Score)

---

## 🚀 How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
jupyter notebook
