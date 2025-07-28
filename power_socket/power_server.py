import socket
import joblib
import numpy as np

# Load trained power model
model = joblib.load("power_model.pkl")

HOST = 'localhost'
PORT = 5001  # Must match the gem5 socket

print("[PowerServer] Starting server...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f"[PowerServer] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                # Expecting features separated by comma, e.g., "15320,416"
                features = list(map(float, data.decode().strip().split(",")))
                prediction = model.predict([features])[0]
                conn.sendall(f"{prediction:.2f}".encode())
            except Exception as e:
                print(f"[PowerServer] Error: {e}")
                conn.sendall(b"0.0")

