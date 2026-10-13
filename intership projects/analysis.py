import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv("sales_data.csv")

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Total revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Product:")
print(product_revenue)

# Best performing product
best_product = product_revenue.idxmax()
best_revenue = product_revenue.max()

print("\nBest Performing Product:", best_product)
print("Revenue:", best_revenue)
# Revenue by region
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Region:")
print(region_revenue)

# Best performing region
best_region = region_revenue.idxmax()
best_region_revenue = region_revenue.max()

print("\nBest Performing Region:", best_region)
print("Revenue:", best_region_revenue)
# Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\nRevenue by Category:")
print(category_revenue)

# Best performing category
best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("\nBest Performing Category:", best_category)
print("Revenue:", best_category_revenue)
# Revenue by Product Chart
plt.figure(figsize=(8, 5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Revenue by Region Chart
plt.figure(figsize=(8, 5))

region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()