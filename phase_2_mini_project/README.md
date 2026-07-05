# 📦 Order Delay Intelligence: Predict, Explain, Recommend

## 📖 Project Overview

This project was completed as part of the **CodeTrade.io AI/ML Internship Mini Project – Phase 2**.

The objective is to analyze an e-commerce dataset, identify factors causing delivery delays, and build machine learning models that can predict whether an order is likely to be delayed. The project combines Data Analysis, SQL, Machine Learning, Model Evaluation, Hyperparameter Tuning, and Explainable AI (SHAP).

---

## 🎯 Business Problem

For an e-commerce company, delayed deliveries can negatively impact customer satisfaction and retention.

This project aims to:

* Analyze order delivery behavior.
* Identify factors contributing to delivery delays.
* Predict delayed orders before delivery.
* Provide business recommendations to reduce future delays.
* Explain model predictions using SHAP.

---

## 📂 Dataset

Dataset Used: **Brazilian E-Commerce Public Dataset by Olist**

Files Used:

* `olist_orders_dataset.csv`
* `olist_order_payments_dataset.csv`
* `olist_customers_dataset.csv`
* `olist_order_items_dataset.csv`
* `olist_products_dataset.csv`

Dataset Source:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite3
* Scikit-Learn
* XGBoost
* SHAP

### Development Environment

* Google Colab
* Jupyter Notebook

---

## 📊 Project Workflow

### Phase 1: Data Audit & Cleaning

* Loaded multiple CSV files
* Checked data types
* Identified missing values
* Removed duplicates
* Converted date columns into datetime format

### Feature Engineering

Created new features such as:

* Delivery Days
* Delay Days
* Purchase Month
* Purchase Weekday
* Delayed (Target Variable)

---

## 📈 Exploratory Data Analysis (EDA)

Generated multiple visualizations including:

1. Delivery Days Distribution
2. Delayed vs Non-Delayed Orders
3. Monthly Order Trends
4. State-wise Delay Analysis
5. Payment Value Analysis
6. Freight Cost vs Delay Relationship

### Key Insights

* Higher freight costs are associated with increased delays.
* Certain states experience higher delivery delays.
* Delivery performance varies across months.
* Larger orders tend to have longer delivery times.
* Logistics-related features significantly impact delays.

---

## 🗄️ SQL Analysis

Cleaned data was loaded into SQLite.

Implemented:

* SELECT
* WHERE
* GROUP BY
* ORDER BY
* Aggregate Functions
* JOIN Operations
* Subqueries

A total of **10 SQL business queries** were created to analyze order behavior and delivery performance.

---

## 🤖 Machine Learning Models

### Baseline Model

**Logistic Regression**

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

---

### Advanced Model

**XGBoost Classifier**

Advantages:

* Handles tabular data efficiently
* Captures non-linear relationships
* Higher predictive performance

---

## 🔄 Cross Validation

Implemented:

* Stratified K-Fold Cross Validation
* Model Stability Analysis

Compared:

* Logistic Regression
* XGBoost

Using:

* Mean F1 Score
* Standard Deviation

---

## ⚙️ Hyperparameter Tuning

Used:

* GridSearchCV

Parameters Tuned:

* n_estimators
* max_depth
* learning_rate

Objective:

* Improve model generalization
* Reduce overfitting

---

## 🔍 Explainable AI (SHAP)

SHAP was used to explain model predictions.

Generated:

* SHAP Summary Plot
* Feature Importance Analysis
* Individual Prediction Explanations

This helps business stakeholders understand why a delivery is predicted to be delayed.

---

## 📋 Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

### Business Focus Metric

**Recall**

Recall is particularly important because missing a delayed order can lead to poor customer experience and operational inefficiencies.

---

## 💡 Business Recommendations

1. Improve logistics performance in high-delay regions.
2. Monitor orders with high freight charges.
3. Allocate resources during peak demand months.
4. Use predictive alerts for high-risk orders.
5. Continuously monitor SHAP-important features.

---

## 📁 Repository Structure

```text
├── README.md
├── Order_Delay_Intelligence.ipynb
├── datasets/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_order_items_dataset.csv
│   └── olist_products_dataset.csv
├── plots/
├── reports/
└── requirements.txt
```

---

## 🚀 How to Run

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/order-delay-intelligence.git
```

### Step 2: Open Google Colab

Upload:

* Order_Delay_Intelligence.ipynb
* Required Dataset Files

### Step 3: Install Dependencies

```python
!pip install xgboost shap
```

### Step 4: Run All Cells

Run the notebook sequentially from top to bottom.

---

## 👨‍💻 Author

**Palak Agarwal**

AI/ML Intern Project

---

## ⭐ Acknowledgement

Special thanks to:

* CodeTrade.io
* Olist Brazilian E-Commerce Dataset
* Scikit-Learn Community
* XGBoost Developers
* SHAP Contributors
