# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load cleaned dataset
# df = pd.read_csv("Grocery_Sales_Cleaned.csv")

# # Set plot style
# sns.set(style="whitegrid")

# # Distribution of Item_Outlet_Sales
# plt.figure(figsize=(10, 5))
# sns.histplot(df["Item_Outlet_Sales"], bins=50, kde=True, color="blue")
# plt.title("Sales Distribution")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
# plt.show()

# # Price vs Sales Scatter Plot
# plt.figure(figsize=(10, 5))
# sns.scatterplot(x=df["Item_MRP"], y=df["Item_Outlet_Sales"], alpha=0.5)
# plt.title("Price vs Sales")
# plt.xlabel("Maximum Retail Price (MRP)")
# plt.ylabel("Sales")
# plt.show()

# # Store Type vs Sales
# plt.figure(figsize=(10, 5))
# sns.boxplot(x=df["Outlet_Type"], y=df["Item_Outlet_Sales"], palette="Set2")
# plt.title("Store Type vs Sales")
# plt.xlabel("Store Type")
# plt.ylabel("Sales")
# plt.xticks(rotation=45)
# plt.show()
