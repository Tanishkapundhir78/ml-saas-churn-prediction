# 📊 Customer Retention Intelligence System (Churn Prediction + Decision Engine)

## 🚀 Project Overview

This project goes beyond traditional churn prediction by building a **Customer Retention Intelligence System**.

Instead of only predicting churn, this system:

* Identifies high-risk customers
* Explains *why* customers churn
* Segments customers into meaningful groups
* Recommends retention strategies
* Evaluates strategies using A/B testing

---

## 🎯 Problem Statement

Customer churn is a major challenge for subscription-based businesses.

Most solutions:

* Predict churn ❌
* Stop there ❌

This project aims to:

> **Predict, understand, and reduce churn using data-driven strategies**

---

## 🧠 Key Features

### 1️⃣ Churn Prediction Model

* Built using machine learning (Logistic Regression, Random Forest)
* Focus on **recall** to capture maximum churn cases
* Handles missing values, encoding, and preprocessing

---

### 2️⃣ Threshold Optimization (Advanced)

* Default threshold (0.5) replaced with optimized threshold
* Used **precision-recall tradeoff**
* Improved detection of churn customers

📌 Outcome:

* Better business decision-making
* Reduced false negatives

---

### 3️⃣ Explainable AI (SHAP)

* Used SHAP for model interpretability
* Identified key churn drivers:

  * Monthly Charges ↑ → higher churn
  * Tenure ↓ → higher churn

📌 Impact:

* Model is no longer a black box
* Provides actionable insights

---

### 4️⃣ Customer Segmentation (KMeans)

* Grouped customers into segments:

  * High-value loyal customers
  * High-risk churn customers
  * Low-engagement users

📌 Impact:

* Enables targeted strategies instead of generic solutions

---

### 5️⃣ Retention Strategy Engine (Business Layer)

* Rule-based system built on top of predictions

Examples:

* High risk → Offer discount
* High charges → Provide cheaper plan
* New customers → Onboarding support

📌 Impact:

* Converts predictions into **business actions**

---

### 6️⃣ A/B Testing Simulation (Advanced)

* Simulated two strategies:

  * Discount Offer
  * Customer Support

📊 Results:

* Discount Offer → **69.36% retention**
* Customer Support → **60.02% retention**

📌 Insight:

* Financial incentives outperform service-based interventions

---

### 7️⃣ Statistical Validation

* Conducted hypothesis testing (T-test)
* Verified statistical significance of results

📌 Impact:

* Ensures decisions are **data-backed, not random**

---

## 📊 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* SHAP
* Matplotlib / Seaborn

---

## 📈 Key Insights

* Customers with **high monthly charges and low tenure** are more likely to churn
* **Discount-based strategies** significantly improve retention
* Segmentation enables **personalized retention strategies**
* Optimizing threshold improves business outcomes

---

## 🧠 Business Impact

This system enables:

* Early identification of churn risk
* Data-driven retention strategies
* Improved customer lifetime value (CLV)
* Reduced revenue loss

---

## 🔥 What Makes This Project Unique

Unlike typical churn projects, this includes:

✅ Prediction
✅ Explainability
✅ Segmentation
✅ Strategy Engine
✅ A/B Testing
✅ Statistical Validation

👉 This makes it a **complete decision intelligence system**

---

## 🚀 Future Improvements

* Real-time deployment using APIs
* Integration with business dashboards
* Personalized offer recommendation using ML
* Time-series churn prediction

---

## 👤 Author

**Tanishka Pundhir**
B.Tech (Artificial Intelligence & Data Science)

---

## ⭐ Conclusion

This project demonstrates how machine learning can move beyond prediction to **actionable business intelligence**, helping organizations not only understand churn but actively reduce it.


