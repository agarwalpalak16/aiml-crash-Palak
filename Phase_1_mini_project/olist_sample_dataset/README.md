# 🛒 E-Commerce Sales Performance Analysis
## Phase 1 Mini Project — Exploratory Data Analysis (EDA)

> **Programme:** CodeTrade.io Industrial Training — Phase 1  
> **Dataset:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)

---

## 📌 Problem Statement

A rapidly growing e-commerce company wants to better understand its sales performance, customer behaviour, and product trends across different regions. As a Data Analyst, this project performs a complete EDA workflow on Olist transaction data to generate actionable business insights.

---

## 🎯 Business Questions Answered

| # | Question |
|---|----------|
| 1 | Which product categories generate the highest revenue? |
| 2 | Which cities/regions contribute the most sales? |
| 3 | Which customer segments provide the highest business value? |
| 4 | What purchasing patterns exist in customer buying behaviour? |
| 5 | Which products show the highest sales volume and revenue? |
| 6 | How do payment methods influence purchasing trends? |
| 7 | Which sellers contribute the most value? |
| 8 | How do review scores vary across categories/regions? |
| 9 | What happens to sales volume across time periods? |
| 10 | Which customers are repeated vs one-time buyers? |
| 11 | What data quality issues appear in the merged dataset? |
| 12 | How reliable is the merge across multiple source files? |

---

## 📁 Repository Structure

```
├── ecommerce_eda.ipynb          ← Main Jupyter Notebook (all 12 questions)
├── README.md                    ← This file
├── report/
│   └── EDA_One_Page_Report.docx ← One-page business report
├── data/                        ← Place Kaggle CSV files here (see below)
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_product_category_name_translation.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── olist_geolocation_dataset.csv
└── charts/                      ← Auto-generated charts (created by notebook)
```

---

## ⬇️ How to Download the Dataset

1. Create a free account at [kaggle.com](https://www.kaggle.com)
2. Go to: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
3. Click the **Download** button (top right)
4. Extract the ZIP file
5. Place all `.csv` files inside a `data/` folder next to the notebook

---

## 🚀 How to Run

### Option 1 — Local (Jupyter)

```bash
# 1. Clone this repo
git clone https://github.com/<your-username>/ecommerce-eda.git
cd ecommerce-eda

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter nbformat

# 3. Launch Jupyter
jupyter notebook ecommerce_eda.ipynb
```

### Option 2 — Google Colab (No install needed)

1. Upload `ecommerce_eda.ipynb` to [colab.research.google.com](https://colab.research.google.com)
2. Upload all CSV files from the `data/` folder
3. Run all cells (`Runtime → Run all`)

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning, merging |
| `numpy` | Numerical operations |
| `matplotlib` | Charts and visualisations |
| `seaborn` | Statistical visualisations |
| `nbformat` | Notebook generation |

Install all at once:
```bash
pip install pandas numpy matplotlib seaborn nbformat
```

---

## 📊 Key Findings Summary

- **Top Revenue Category:** Health & beauty / watches & gifts dominate platform revenue
- **Geographic Concentration:** São Paulo state accounts for the largest share of sales — a classic Pareto pattern
- **Customer Retention Challenge:** >90% of customers are one-time buyers — the biggest growth lever
- **Payment Behaviour:** Credit cards dominate; boleto users are price-sensitive
- **Seasonal Peak:** November (Black Friday) shows the strongest sales spike
- **Merge Reliability:** >98% join completeness across all key tables — dataset is analysis-ready

---

## 📋 Evaluation Criteria Coverage

| Criteria | Weight | Covered |
|----------|--------|---------|
| Problem Understanding | 10% | ✅ Step 1 — Business questions defined |
| Data Loading & Preparation | 20% | ✅ Step 2 — All 9 CSVs loaded & explored |
| Data Cleaning Quality | 20% | ✅ Step 3 — Full cleaning log documented |
| Exploratory Data Analysis | 20% | ✅ Step 4 — All 12 questions answered |
| Visualisations | 15% | ✅ Step 5 — Labelled charts for every question |
| Business Insights | 15% | ✅ Step 6 — Observation → Insight for each |

---

## 👤 Author

Palak Agarwal

Industrial Training — Phase 1 | CodeTrade.io  
*This project is for educational purposes using a publicly available dataset.*
