import pandas as pd
# Load the dataset
df = pd.read_excel("Grocery_sales.xlsx") 

# Display basic information
print("Dataset Info:")
print(df.info())

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display basic statistics
print("\nDataset Statistics:")
print(df.describe())