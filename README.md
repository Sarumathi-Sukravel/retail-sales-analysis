# 🛒 Retail Sales Data Analysis

A complete exploratory data analysis (EDA) project on retail sales data — covering monthly trends, category & regional performance, discount behavior, payment preferences, and customer satisfaction patterns.

## 📊 Overview

This project analyzes 5,000 synthetic but realistic retail orders across India (2024–2025) to answer key business questions:

- Which product categories and regions drive the most revenue?
- How do discounts affect order volume?
- What payment methods do customers prefer?
- Are ratings consistent across category and region?

## 🛠️ Tech Stack

- **Python 3**
- **Pandas** – data wrangling
- **Matplotlib / Seaborn** – visualization
- **NumPy** – synthetic data generation

## 🚀 How to Run

```bash
pip install pandas matplotlib seaborn numpy
cd data && python generate_data.py && cd ..
python analysis.py
```

## 📈 Key Insights

- **Electronics** is the top revenue-generating category, driven by high unit prices.
- **West region** leads in total net sales.
- **UPI** is the most preferred payment method — reflecting India's digital payment trends.
- Orders with **0% discount** are still the most frequent, suggesting price isn't the only purchase driver.
- Customer ratings stay fairly consistent (~4.0–4.3) across categories and regions, indicating stable service quality.

## 📌 Sample Visuals

| Monthly Trend | Category Sales | Payment Share |
|---|---|---|
| ![trend](monthly_sales_trend.png) | ![category](sales_by_category.png) | ![payment](payment_mode_share.png) |

## 🔮 Possible Extensions

- Add a Streamlit dashboard for interactive filtering
- Forecast next quarter's sales using time series models
- Segment customers using RFM analysis

---
*Part of my Data Analytics portfolio — [Sarumathi Sukravel](https://github.com/Sarumathi-Sukravel)*
