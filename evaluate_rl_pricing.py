import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Initial & RL-Updated Prices
comparison_df = pd.read_csv("RL_Pricing_Comparison.csv")  # Ensure it has "Initial_Price" & "New_Price"

# Simulate sales & cost (assuming additional columns exist in dataset)
comparison_df["Sales_Original"] = np.random.randint(50, 200, size=len(comparison_df))  # Random sales data
comparison_df["Sales_RL"] = np.random.randint(50, 200, size=len(comparison_df))  # RL sales data (for comparison)
comparison_df["Cost"] = np.random.uniform(10, 50, size=len(comparison_df))  # Random cost data per unit

# Compute Revenue Before & After RL Pricing
comparison_df["Revenue_Original"] = comparison_df["Initial_Price"] * comparison_df["Sales_Original"]
comparison_df["Revenue_RL"] = comparison_df["New_Price"] * comparison_df["Sales_RL"]

# 1️⃣ Revenue Improvement (% Change)
comparison_df["Revenue_Change_%"] = ((comparison_df["Revenue_RL"] - comparison_df["Revenue_Original"]) / comparison_df["Revenue_Original"]) * 100
avg_revenue_change = comparison_df["Revenue_Change_%"].mean()

# 2️⃣ Profit Margin Impact
comparison_df["Profit_Original"] = (comparison_df["Initial_Price"] - comparison_df["Cost"]) * comparison_df["Sales_Original"]
comparison_df["Profit_RL"] = (comparison_df["New_Price"] - comparison_df["Cost"]) * comparison_df["Sales_RL"]
comparison_df["Profit_Change_%"] = ((comparison_df["Profit_RL"] - comparison_df["Profit_Original"]) / comparison_df["Profit_Original"]) * 100
avg_profit_change = comparison_df["Profit_Change_%"].mean()

# 3️⃣ Price Elasticity Impact
comparison_df["PED"] = np.random.uniform(-2, 2, size=len(comparison_df))  # Placeholder PED values
comparison_df["PED_Impact"] = (comparison_df["New_Price"] - comparison_df["Initial_Price"]) / comparison_df["Initial_Price"] * comparison_df["PED"]
avg_ped_impact = comparison_df["PED_Impact"].mean()

# 4️⃣ Exploration vs. Exploitation Balance
comparison_df["Price_Change"] = abs(comparison_df["New_Price"] - comparison_df["Initial_Price"])
exploration_rate = (comparison_df["Price_Change"] > comparison_df["Initial_Price"] * 0.1).mean() * 100  # % of major price changes

# **📊 Print Evaluation Results**
print("\n📊 RL Pricing Model Evaluation Results:")
print(f"✅ Revenue Improvement: {avg_revenue_change:.2f}%")
print(f"✅ Profit Margin Impact: {avg_profit_change:.2f}%")
print(f"✅ Price Elasticity Impact: {avg_ped_impact:.2f}")
print(f"✅ Exploration Rate: {exploration_rate:.2f}% (Major price changes)")

# **📁 Save Final Evaluation Results**
comparison_df.to_csv("Final_RL_Pricing_Evaluation.csv", index=False)
print("\n📁 Evaluation results saved to Final_RL_Pricing_Evaluation.csv")

# **📊 Visualizing Price Adjustments**
plt.figure(figsize=(12, 6))
sns.barplot(x="Item_Type", y="Revenue_Change_%", data=comparison_df, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("Revenue Change (%) by RL Model")
plt.axhline(0, color='black', linestyle="--")
plt.xlabel("Item Type")
plt.ylabel("Revenue Change (%)")
plt.show()

