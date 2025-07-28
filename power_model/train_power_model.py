import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib  # For saving model

# Load CSV
#df = pd.read_csv("power_data.csv", header=None)
df = pd.read_csv("power_data.csv")
print(df.head())
# Rename columns
df.columns = [
    "time", "voltage", "current", "power", "flag",
    "0_v", "0_a", "0_p", "0_flag", "0_in",
    "1_v", "1_a", "1_p", "1_flag", "1_in",
    "chksum1", "chksum2"
]

# Use just voltage and current for the model
X = df[['voltage', 'current']]
y = df['power']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Print results
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R^2 Score:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "power_model.pkl")
print("Model saved as power_model.pkl")

