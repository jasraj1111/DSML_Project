import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("Grocery_Sales_Final.csv")

# Selecting features (X) and target (y)
X = df.drop(columns=["Item_Outlet_Sales", "Item_Identifier"])  # Drop target & ID column
y = df["Item_Outlet_Sales"]

# One-hot encoding categorical variables
X = pd.get_dummies(X, drop_first=True)

# Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize Data for Linear Regression (Random Forest doesn't need this)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize Models
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
lr_model = LinearRegression()

# Train both models
rf_model.fit(X_train, y_train)
lr_model.fit(X_train_scaled, y_train)

# Predictions
rf_pred = rf_model.predict(X_test)
lr_pred = lr_model.predict(X_test_scaled)

# Evaluate Performance
def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    
    print(f"\n📊 {model_name} Model Performance:")
    print(f"MAE  (Mean Absolute Error)    : {mae:.2f}")
    print(f"MSE  (Mean Squared Error)     : {mse:.2f}")
    print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
    print(f"R² Score                     : {r2:.4f}")
    
    return r2

# Compare models
rf_r2 = evaluate_model(y_test, rf_pred, "Random Forest Regressor")
lr_r2 = evaluate_model(y_test, lr_pred, "Linear Regression")

# Choose the Best Model
best_model = "Random Forest" if rf_r2 > lr_r2 else "Linear Regression"
print(f"\n🏆 The better model is: {best_model}")

# Hyperparameter Tuning with GridSearchCV
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

# Initialize Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Perform Grid Search
rf_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, verbose=2, n_jobs=-1)

# Train with the best parameters
rf_search.fit(X_train, y_train)

# Get best model
best_rf = rf_search.best_estimator_

# Predict with optimized model
best_rf_pred = best_rf.predict(X_test)

# Evaluate optimized model
evaluate_model(y_test, best_rf_pred, "Optimized Random Forest")

# Print the best parameters
print("\n🔎 Best Parameters Found:", rf_search.best_params_)
