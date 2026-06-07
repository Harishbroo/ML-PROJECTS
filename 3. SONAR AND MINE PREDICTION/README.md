# 💎 Sonar Rock vs. Mine Prediction

This project processes underwater sonar signals to determine whether a detected object is a harmless rock or a metal military mine. The dataset consists of sonar frequencies bounced off different surfaces at various angles.

## 📊 Project Details
* **Model Type:** Binary Classification (Rock vs. Mine)
* **Dataset Used:** `sonardata.csv`
* **Key Focus:** High-dimensional data processing and analyzing continuous frequency patterns.

## 🛠️ Key Steps Implemented
1. **Data Exploration:** Analyzed the 60 continuous numerical features representing sonar frequencies.
2. **Data Preprocessing:** Checked for missing values and split data into training and testing sets.
3. **Model Selection:** Trained a binary classification model (such as Logistic Regression) to detect patterns.
4. **Evaluation:** Evaluated accuracy metrics to ensure reliable detection rates for security applications.

## 📁 File Structure
* `sonardata.csv`: The dataset containing sonar frequency responses.
* `rockvsmine.ipynb`: Jupyter notebook with the complete data analysis, training workflow, and model evaluation.
