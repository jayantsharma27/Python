import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load data
data = pd.read_excel("data/online_retail_II.xlsx", sheet_name="Year 2010-2011")
data.dropna(subset=["Customer ID"], inplace=True)
data = data[data["Quantity"] > 0]
data["TotalPrice"] = data["Quantity"] * data["Price"]

# RFM features
rfm = data.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (data["InvoiceDate"].max() - x.max()).days,
    "Invoice": "nunique",
    "TotalPrice": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

# Model training
X = rfm[["Recency", "Frequency"]]
y = rfm["Monetary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "clv_model.pkl")
print("✅ Model trained and saved!")
