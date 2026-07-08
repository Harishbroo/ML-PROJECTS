# 🛒 Mall Customer Segmentation

## 📖 Overview

This project segments retail customers into different groups using **K-Means Clustering**, an unsupervised Machine Learning algorithm. The application is built with **Streamlit**, containerized using **Docker**, and deployed on **Render**.

---

## 🌐 Live Demo

🚀 **Live Application:** https://customer-segmentation-cgbg.onrender.com

---

## 📊 Dataset

- Dataset: `Mall_Customers.csv`
- Model Type: Unsupervised Learning
- Algorithm: K-Means Clustering

---

## 📁 Project Files

- `customerseg.ipynb` – Data preprocessing, EDA, Elbow Method, and K-Means clustering
- `Mall_Customers.csv` – Dataset
- `kmeans_model.pkl` – Trained K-Means model
- `app.py` – Streamlit web application
- `requirements.txt` – Python dependencies
- `Dockerfile` – Docker configuration

---

## ⚙️ Workflow

- Data loading and inspection
- Exploratory Data Analysis (EDA)
- Feature selection
- Finding the optimal number of clusters using the Elbow Method
- K-Means model training
- Customer segmentation
- Cluster visualization

---

## 🤖 Algorithm Used

- K-Means Clustering

---

## 📈 Results

- Identified **5 distinct customer segments**
- Visualized customer groups based on **Annual Income** and **Spending Score**
- Useful for targeted marketing and customer analysis

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
docker build -t harishprj/customer-segmentation .
```

Run the Docker container:

```bash
docker run -p 8001:8501 harishprj/customer-segmentation
```

---

## 👨‍💻 Author

**Harish Parajuli**
