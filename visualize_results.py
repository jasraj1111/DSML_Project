import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Evaluation Results
comparison_df = pd.read_csv("Final_RL_Pricing_Evaluation.csv")

# **📊 Visualization 1: Revenue Improvement**
plt.figure(figsize=(12, 6))
sns.barplot(x="Item_Type", y="Revenue_Change_%", data=comparison_df, palette="coolwarm")
plt.xticks(rotation=90)
plt.title("📈 Revenue Change (%) by RL Model")
plt.axhline(0, color='black', linestyle="--")
plt.xlabel("Item Type")
plt.ylabel("Revenue Change (%)")
plt.show()

# **📊 Visualization 2: Profit Margin Impact**
plt.figure(figsize=(12, 6))
sns.barplot(x="Item_Type", y="Profit_Change_%", data=comparison_df, palette="viridis")
plt.xticks(rotation=90)
plt.title("💰 Profit Margin Change (%) by RL Model")
plt.axhline(0, color='black', linestyle="--")
plt.xlabel("Item Type")
plt.ylabel("Profit Change (%)")
plt.show()

# **📊 Visualization 3: Price Elasticity Impact**
plt.figure(figsize=(12, 6))
sns.histplot(comparison_df["PED_Impact"], bins=20, kde=True, color="purple")
plt.title("📉 Distribution of Price Elasticity Impact")
plt.xlabel("PED Impact Score")
plt.ylabel("Frequency")
plt.axvline(comparison_df["PED_Impact"].mean(), color='red', linestyle="--", label="Mean PED Impact")
plt.legend()
plt.show()

# **📊 Visualization 4: Exploration vs. Exploitation Balance**
plt.figure(figsize=(12, 6))
sns.histplot(comparison_df["Price_Change"], bins=20, kde=True, color="orange")
plt.title("🎢 Exploration vs. Exploitation: Price Change Distribution")
plt.xlabel("Absolute Price Change")
plt.ylabel("Frequency")
plt.axvline(comparison_df["Price_Change"].mean(), color='blue', linestyle="--", label="Mean Price Change")
plt.legend()
plt.show()

