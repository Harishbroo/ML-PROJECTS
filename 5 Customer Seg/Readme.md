# 🛒 Mall Customer Segmentation

This project uses unsupervised machine learning to group retail customers into distinct segments. By clustering customers based on their annual income and spending score, businesses can design data-driven, targeted marketing strategies.

## 📊 Project Details
* **Model Type:** Unsupervised Clustering
* **Dataset Used:** `Mall_Customers.csv`
* **Algorithm Used:** K-Means Clustering

## 🛠️ Key Steps Implemented
1. **Exploratory Data Analysis (EDA):** Visualized distributions of age, annual income, and spending scores.
2. **Finding Optimal Clusters:** Utilized the **Elbow Method** (Within-Cluster Sum of Squares) to determine the ideal number of customer segments.
3. **Model Training:** Trained the K-Means algorithm using Scikit-Learn to segment data points.
4. **Cluster Visualization:** Plotted the final segments on a 2D scatter plot, clearly identifying customer groups (e.g., high-income/low-spend, high-income/high-spend).

## 📁 File Structure
* `Mall_Customers.csv`: The customer database containing spending details.
* `customerseg.ipynb`: Jupyter notebook containing the preprocessing, WCSS elbow curve, and K-Means segmentation code.
