import joblib
import numpy as np

# Load the trained model
model = joblib.load("power_model.pkl")

# Example stats from stats.txt
sim_insts = 31552962
num_cycles = 50437704

# Feature vector (adjust according to your model's expected inputs)
features = np.array([[sim_insts, num_cycles]])

# Predict power
predicted_power = model.predict(features)[0]
print(f"Estimated Average Power: {predicted_power:.2f} mW")

