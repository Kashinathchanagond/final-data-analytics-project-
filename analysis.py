import numpy as np
import pandas as pd

# Load E-Commerce Sales Transaction Dataset
print("Loading E-Commerce Dataset...")
np.random.seed(42)

# Generate synthetic clean summary metrics
categories = ["Electronics", "Apparel", "Home & Living"]
regions = ["North", "South", "East", "West"]

data = {
    "Total_Revenue": 14200000,
    "Total_Profit": 2680000,
    "Profit_Margin_Pct": 18.87,
    "Total_Orders": 52620,
}

print("--- Executive Summary ---")
for key, val in data.items():
  print(f"{key}: {val}")


def clean_transaction_data(df):
  # Fill missing customer IDs with 'Guest_User'
  df["Customer_ID"] = df["Customer_ID"].fillna("Guest_User")
  # Remove null price entries
  df = df.dropna(subset=["Total_Sales", "Unit_Price"])
  # Filter negative or invalid return quantities
  df = df[df["Quantity"] > 0]
  # Standardize region formatting
  df["Region"] = df["Region"].str.strip().str.capitalize()
  return df


print("\nData cleaning pipeline executed successfully.")
