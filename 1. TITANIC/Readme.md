# 🚢 Titanic Survival Prediction

## 📖 Overview
This project predicts whether a passenger survived the Titanic disaster using Machine Learning. The application is built with Streamlit, Dockerized for portability, and deployed on Render.

## 📊 Dataset
- Source: Kaggle Titanic Dataset
- Features: Age, Sex, Pclass, Fare, Embarked, FamilySize, Title, etc.

## ⚙️ Workflow
- Data cleaning (handling missing values)
- Feature engineering (Title, FamilySize, IsAlone)
- Encoding categorical variables
- Model training and evaluation
- Prediction using the best trained model

## 🤖 Models Used
- Logistic Regression
- Decision Tree
- Random Forest (Best Model)

## 🏆 Kaggle Score
- Public Score: **0.77033**
- Private Score: **0.76510**

## 📈 Results
- Best Accuracy: **~77%**
- Improved performance after feature engineering

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Docker
- Render

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🐳 Docker

Build the Docker image:

```bash
docker build -t harishprj/titanic .
```

Run the container:

```bash
docker run -p 8001:8501 harishprj/titanic
```

## 🌐 Live Demo

**Render:**  
https://titanic-survival-jip1.onrender.com

## 👨‍💻 Author

**Harish Parajuli**
