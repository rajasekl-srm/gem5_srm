import joblib
import numpy as np

model = joblib.load("power_model.pkl")

# Example: Voltage=15300 mV, Current=420 mA
input_data = np.array([[15300, 420]])
predicted_power = model.predict(input_data)

print(f"Predicted Power (mW): {predicted_power[0]:.2f}")

