"""
Retail Sales Data Analysis
Explores sales trends, top categories/regions, discount impact, and payment behavior.
Run: python analysis.py
Charts are saved into visuals/
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 110

df = pd.read_csv("data/retail_sales.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

print("=" * 60)
print("RETAIL SALES DATASET OVERVIEW")
print("=" * 60)
print(f"Rows: {len(df):,} | Date range: {df.order_date.min().date()} to {df.order_date.max().date()}")
print(f"Total net sales: ₹{df.net_sales.sum():,.0f}")
print(f"Average order value: ₹{df.net_sales.mean():,.0f}")
print()

# 1. Monthly sales trend
monthly = df.groupby("month")["net_sales"].sum()
plt.figure(figsize=(11, 5))
monthly.plot(kind="line", marker="o", color="#2563eb")
plt.title("Monthly Net Sales Trend")
plt.ylabel("Net Sales (₹)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_sales_trend.png")
plt.close()

# 2. Sales by category
cat_sales = df.groupby("category")["net_sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(9, 5))
sns.barplot(x=cat_sales.values, y=cat_sales.index, palette="Blues_r")
plt.title("Net Sales by Category")
plt.xlabel("Net Sales (₹)")
plt.tight_layout()
plt.savefig("visuals/sales_by_category.png")
plt.close()
print("Top category:", cat_sales.index[0], f"(₹{cat_sales.iloc[0]:,.0f})")

# 3. Regional performance
region_sales = df.groupby("region")["net_sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(7, 5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="viridis")
plt.title("Net Sales by Region")
plt.ylabel("Net Sales (₹)")
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.close()
print("Top region:", region_sales.index[0], f"(₹{region_sales.iloc[0]:,.0f})")

# 4. Discount impact on order volume
disc_orders = df.groupby("discount_pct")["order_id"].count()
plt.figure(figsize=(8, 5))
sns.barplot(x=disc_orders.index, y=disc_orders.values, palette="Oranges")
plt.title("Order Count by Discount Level")
plt.xlabel("Discount %")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("visuals/discount_vs_orders.png")
plt.close()

# 5. Payment mode share
payment_share = df["payment_mode"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(payment_share.values, labels=payment_share.index, autopct="%1.1f%%",
        colors=sns.color_palette("pastel"))
plt.title("Payment Mode Share")
plt.tight_layout()
plt.savefig("visuals/payment_mode_share.png")
plt.close()
print("Most used payment mode:", payment_share.index[0])

# 6. Category vs average rating heatmap
pivot = df.pivot_table(values="customer_rating", index="category", columns="region", aggfunc="mean")
plt.figure(figsize=(8, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={"label": "Avg Rating"})
plt.title("Average Customer Rating: Category x Region")
plt.tight_layout()
plt.savefig("visuals/rating_heatmap.png")
plt.close()

print()
print("All charts saved to visuals/")
print("=" * 60)
