# ================================
# Bot Error Classifier — Version 1
# ================================

# Your list of errors (use your real ones!)
errors = [
    "Timeout",
    "Login Failed", 
    "Timeout",
    "System Error",
    "Timeout",
    "Login Failed",
    "Data Not Found",
    "System Error"
]

print(f"Total errors to classify: {len(errors)}")
print("=" * 40)

# Loop through every error and classify it
for error in errors:
    if error == "Timeout":
        category = "🌐 Network Issue"
    elif error == "Login Failed":
        category = "🔐 Auth Issue"
    elif error == "Data Not Found":
        category = "📂 Data Issue"
    else:
        category = "⚙️  System Issue"
    
    print(f"  {error:<20} → {category}")

print("=" * 40)
