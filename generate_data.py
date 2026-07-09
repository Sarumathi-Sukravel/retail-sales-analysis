"""
Generates a synthetic but realistic retail sales dataset for analysis.
Run: python generate_data.py
Output: retail_sales.csv
"""
import pandas as pd
import numpy as np

np.random.seed(42)

n_rows = 5000
categories = ["Electronics", "Clothing", "Home & Kitchen", "Beauty", "Sports", "Books", "Toys"]
regions = ["South", "North", "East", "West"]
cities = {
    "South": ["Chennai", "Bengaluru", "Hyderabad", "Coimbatore"],
    "North": ["Delhi", "Chandigarh", "Jaipur", "Lucknow"],
    "East": ["Kolkata", "Patna", "Bhubaneswar", "Guwahati"],
    "West": ["Mumbai", "Pune", "Ahmedabad", "Surat"],
}
payment_modes = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery", "Net Banking"]

dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")
order_dates = np.random.choice(dates, size=n_rows)

rows = []
for i in range(n_rows):
    category = np.random.choice(categories, p=[0.22, 0.18, 0.15, 0.12, 0.13, 0.10, 0.10])
    region = np.random.choice(regions)
    city = np.random.choice(cities[region])
    unit_price = {
        "Electronics": np.random.uniform(1500, 60000),
        "Clothing": np.random.uniform(300, 4000),
        "Home & Kitchen": np.random.uniform(200, 8000),
        "Beauty": np.random.uniform(150, 3000),
        "Sports": np.random.uniform(300, 12000),
        "Books": np.random.uniform(150, 1200),
        "Toys": np.random.uniform(200, 3500),
    }[category]
    quantity = np.random.randint(1, 6)
    discount_pct = np.random.choice([0, 5, 10, 15, 20, 25], p=[0.35, 0.2, 0.2, 0.12, 0.08, 0.05])
    gross = unit_price * quantity
    discount_amt = gross * discount_pct / 100
    net_sales = gross - discount_amt
    rating = np.clip(np.random.normal(4.1, 0.7), 1, 5)

    rows.append({
        "order_id": f"ORD{100000 + i}",
        "order_date": pd.Timestamp(order_dates[i]).date(),
        "category": category,
        "region": region,
        "city": city,
        "unit_price": round(unit_price, 2),
        "quantity": quantity,
        "discount_pct": discount_pct,
        "gross_sales": round(gross, 2),
        "net_sales": round(net_sales, 2),
        "payment_mode": np.random.choice(payment_modes, p=[0.35, 0.22, 0.18, 0.15, 0.10]),
        "customer_rating": round(rating, 1),
    })

df = pd.DataFrame(rows).sort_values("order_date").reset_index(drop=True)
df.to_csv("retail_sales.csv", index=False)
print(f"Generated {len(df)} rows -> retail_sales.csv")
