import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Grocery_Sales_Cleaned.csv")

# Create new features
df["Item_Age"] = 2024 - df["Outlet_Establishment_Year"]  # Assuming current year is 2024
df["Item_Price_Per_Visibility"] = df["Item_MRP"] / (df["Item_Visibility"] + 0.0001)  # Avoid division by zero

# Save updated dataset
df.to_csv("Grocery_Sales_Featured.csv", index=False)

print("Feature Engineering Done! New Features Added:")
print(df[["Item_Age", "Item_Price_Per_Visibility"]].head())

# Encoding categorical features
categorical_cols = ["Item_Fat_Content", "Outlet_Identifier", "Outlet_Size", "Outlet_Location_Type", "Outlet_Type"]
encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

# Save final dataset
df.to_csv("Grocery_Sales_Final.csv", index=False)

print("Categorical Encoding Done!")

