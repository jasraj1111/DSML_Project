import pandas as pd

# Load dataset
df = pd.read_excel("Grocery_sales.xlsx") 

# Fill missing Item_Weight with mean weight of the same Item_Type
df["Item_Weight"] = df.groupby("Item_Type")["Item_Weight"].transform(lambda x: x.fillna(x.mean()))

# Fill missing Outlet_Size based on Outlet_Type mode
outlet_size_mode = df.groupby("Outlet_Type")["Outlet_Size"].agg(lambda x: x.mode()[0])
df["Outlet_Size"] = df["Outlet_Size"].fillna(df["Outlet_Type"].map(outlet_size_mode))

# Verify missing values are handled
print("Missing Values After Cleaning:")
print(df.isnull().sum())


# Standardizing Item_Fat_Content values
df["Item_Fat_Content"] = df["Item_Fat_Content"].replace({
    "low fat": "Low Fat",
    "LF": "Low Fat",
    "reg": "Regular"
})

# Verify unique values
print("Unique values in Item_Fat_Content after cleaning:", df["Item_Fat_Content"].unique())

# Save cleaned dataset
df.to_csv("Grocery_Sales_Cleaned.csv", index=False)
