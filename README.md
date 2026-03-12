# ml-saas-churn-prediction
# SaaS Customer Churn Prediction

## Project Overview
Customer churn is one of the biggest challenges faced by Software-as-a-Service (SaaS) companies. Retaining existing customers is often more cost-effective than acquiring new ones.

This project builds a machine learning model to predict whether a customer is likely to churn based on behavioral and subscription data. The goal is to help businesses identify at-risk customers early and take proactive retention actions.

The project also demonstrates a full end-to-end data science workflow including data analysis, feature engineering, machine learning modeling, model evaluation, and deployment.

---

## Business Problem

In SaaS companies, churn occurs when a customer stops using a service or cancels their subscription. High churn rates can significantly impact revenue and growth.

By predicting churn in advance, companies can:
- Identify customers likely to leave
- Offer targeted retention strategies
- Improve product engagement
- Reduce revenue loss

---

## Project Objectives

- Perform exploratory data analysis (EDA) on customer data
- Identify key factors contributing to churn
- Build machine learning models to predict churn
- Evaluate model performance using appropriate metrics
- Deploy the model as an interactive web application

---

## Dataset

The project uses a public SaaS churn dataset containing customer information such as:

- Customer demographics
- Subscription details
- Product usage patterns
- Support interaction history
- Payment information

Target variable:
- **Churn** (1 = customer left, 0 = customer retained)

---

## Tech Stack

Programming Language:
- Python

Data Analysis:
- Pandas
- NumPy

Data Visualization:
- Matplotlib
- Seaborn

Machine Learning:
- Scikit-learn
- XGBoost (optional)

Model Explainability:
- SHAP

Deployment:
- Streamlit

Version Control:
- Git & GitHub

---

## Project Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Interpretation
8. Deployment with Streamlit

---

## Machine Learning Models

The following models will be explored:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting / XGBoost

Models will be compared using evaluation metrics to select the best performing model.

---

## Evaluation Metrics

Since churn prediction is a classification problem, the following metrics will be used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

Special focus will be given to **Recall**, as identifying customers likely to churn is crucial for retention strategies.

---

## Expected Insights

The analysis aims to uncover patterns such as:

- How product usage affects churn
- Relationship between subscription length and retention
- Impact of customer support interactions
- Key features that influence churn behavior

---

## Project Structure
saas-churn-prediction-ml

data/
raw/
processed/

notebooks/
01_data_exploration.ipynb
02_feature_engineering.ipynb
03_model_training.ipynb

src/
data_preprocessing.py
feature_engineering.py
train_model.py
predict.py

models/
churn_model.pkl

app/
streamlit_app.py

README.md
requirements.txt



---

## Future Improvements

Possible extensions of the project include:

- Handling class imbalance using SMOTE
- Hyperparameter tuning using GridSearchCV
- Customer segmentation using clustering
- Building a recommendation system for retention
- Deploying the model using cloud services

---

## Author

Tanishka Pundhir


