import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Grocery_Sales_Final.csv")

# Group by Item_Type to analyze price sensitivity
grouped_df = df.groupby("Item_Type")[["Item_MRP", "Item_Outlet_Sales"]].mean().reset_index()

# Compute % change in price and sales
# Shift data to get previous values for comparison
grouped_df['MRP_prev'] = grouped_df['Item_MRP'].shift(1)
grouped_df['Sales_prev'] = grouped_df['Item_Outlet_Sales'].shift(1)

grouped_df.dropna(inplace=True)  # Remove NaN values from shifting

grouped_df['% Change in Price'] = ((grouped_df['Item_MRP'] - grouped_df['MRP_prev']) / grouped_df['MRP_prev']) * 100
grouped_df['% Change in Sales'] = ((grouped_df['Item_Outlet_Sales'] - grouped_df['Sales_prev']) / grouped_df['Sales_prev']) * 100

grouped_df['PED'] = grouped_df['% Change in Sales'] / grouped_df['% Change in Price']

# Classify items as Elastic, Inelastic, or Unit Elastic
def classify_ped(ped):
    if ped < -1:
        return "Elastic (Price-Sensitive)"
    elif ped > -1:
        return "Inelastic (Less Price-Sensitive)"
    else:
        return "Unit Elastic"

grouped_df['PED Category'] = grouped_df['PED'].apply(classify_ped)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(data=grouped_df, x="Item_Type", y="PED", hue="PED Category", palette="coolwarm")
plt.axhline(-1, linestyle="--", color="black", label="Elasticity Threshold")
plt.xticks(rotation=90)
plt.xlabel("Item Type")
plt.ylabel("Price Elasticity of Demand (PED)")
plt.title("Price Elasticity Analysis by Product Type")
plt.legend()
plt.show()

# Save results to CSV
grouped_df[['Item_Type', 'Item_MRP', 'PED']].to_csv('PED_Results.csv', index=False)

# Display results
grouped_df.sort_values(by="PED", ascending=True)