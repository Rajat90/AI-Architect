import os
try:
    os.makedirs("reports1", exist_ok=True)
except FileNotFoundError as e:
    print(f"Directory error: {e}")