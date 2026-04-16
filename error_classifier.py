# ============================================
# Bot Error Classifier V2 — With Dictionaries
# ============================================

# Step 1: Define error categories as a dictionary
# Key   = error text from log file
# Value = human readable category name

error_categories = {
    "Timeout"           : "🌐 Network Issue",
    "Connection Refused": "🌐 Network Issue",
    "Login Failed"      : "🔐 Auth Issue",
    "Permission Denied" : "🔐 Auth Issue",
    "Data Not Found"    : "📂 Data Issue",
    "System Error"      : "⚙️  System Issue",
    "Memory Error"      : "⚙️  System Issue",
}

# Step 2: Set up a results counter dictionary
# We'll count how many errors fall in each category
category_counts = {
    "🌐 Network Issue" : 0,
    "🔐 Auth Issue"    : 0,
    "📂 Data Issue"    : 0,
    "⚙️  System Issue"  : 0,
    "❓ Unknown"        : 0,   # ← NEW: catches anything unrecognised
}

# Step 3: Read the log file
print("🤖 Bot Error Classifier V2 Starting...")
print("=" * 65)

with open("bot_logs.txt", "r") as file:
    lines = file.readlines()

print(f"📂 Loaded {len(lines)} log entries")
print()

# Step 4: Classify each error using dictionary lookup
unknown_errors = []   # track errors we don't recognise

print(f"{'BOT':<15} {'ERROR':<25} {'CATEGORY'}")
print("-" * 65)

for line in lines:
    parts    = line.strip().split(" | ")
    bot_name = parts[0]
    error    = parts[2]

    # Dictionary lookup — cleaner than if/elif chain!
    if error in error_categories:
        category = error_categories[error]
    else:
        category = "❓ Unknown"
        if error not in unknown_errors:
            unknown_errors.append(error)   # track new unknown types

    # Update the counter
    category_counts[category] += 1

    print(f"{bot_name:<15} {error:<25} {category}")

# Step 5: Print summary
print("=" * 65)
print()
print("📊 CLASSIFICATION SUMMARY")
print("=" * 40)

for category, count in category_counts.items():
    if count > 0:   # only show categories that have errors
        bar = "█" * count   # visual bar chart!
        print(f"  {category:<22}: {count:>3}  {bar}")

print("=" * 40)
print(f"  📋 Total Errors: {len(lines)}")

# Step 6: Alert for unknown errors
if unknown_errors:
    print()
    print("⚠️  UNKNOWN ERROR TYPES DETECTED:")
    print("   These need to be added to your classifier:")
    for unknown in unknown_errors:
        print(f"   → '{unknown}'")
else:
    print()
    print("✅ All errors successfully classified!")

# Step 7: Save report
with open("classification_report_v2.txt", "w", encoding="utf-8") as report:
    report.write("BOT ERROR CLASSIFICATION REPORT V2\n")
    report.write("=" * 40 + "\n")
    for category, count in category_counts.items():
        if count > 0:
            report.write(f"{category}: {count}\n")
    report.write(f"\nTotal: {len(lines)}\n")
    if unknown_errors:
        report.write("\nUNKNOWN ERRORS FOUND:\n")
        for e in unknown_errors:
            report.write(f"  - {e}\n")

print()
print("✅ Report saved to classification_report_v2.txt")