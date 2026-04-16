# ============================================
# Bot Error Classifier V3 — Functions Based
# ============================================

# ---- ALL FUNCTIONS DEFINED AT TOP ----

def load_log_file(filename):
    """Reads a log file and returns list of lines."""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"📂 Loaded {len(lines)} entries from {filename}")
    return lines

def parse_log_line(line):
    """Splits one log line into bot_name, timestamp, error."""
    parts = line.strip().split(" | ")
    bot_name  = parts[0]
    timestamp = parts[1]
    error     = parts[2]
    return bot_name, timestamp, error

def clasify_error(error_text):
    """Returns the category for a given error type."""
    error_categories = {
        "Timeout"            : "🌐 Network Issue",
        "Connection Refused" : "🌐 Network Issue",
        "Login Failed"       : "🔐 Auth Issue",
        "Permission Denied"  : "🔐 Auth Issue",
        "Data Not Found"     : "📂 Data Issue",
        "System Error"       : "⚙️  System Issue",
        "Memory Error"       : "⚙️  System Issue",  
    }
    if error_text in error_categories:
        return error_categories[error_text]
    else:
        return "❓ Unknown"
    
def print_results(results):
    """Prints the classified results as a table."""
    print()
    print(f"{'BOT':<15} {'ERROR':<25} {'CATEGORY'}")
    print("-" * 65)
    for bot_name, error, category in results:
        print(f"{bot_name:<15} {error:<25} {category}")
    print("=" * 65)    

def print_summary(category_counts, total):
    """Prints the summary with visual bar chart."""
    print()
    print("📊 CLASSIFICATION SUMMARY")
    print("=" * 45)
    for category, count in category_counts.items():
        if count > 0:
            bar = "█" * count
            print(f"  {category:<22}: {count:>3}  {bar}")
    print("=" * 45)
    print(f"  📋 Total Errors: {total}")    


def save_report(filename, category_counts, unknown_errors, total):
    """Saves classification report to a text file."""
    with open(filename, "w", encoding="utf-8") as report:
        report.write("BOT ERROR CLASSIFICATION REPORT V3\n")
        report.write("=" * 40 + "\n")
        for category, count in category_counts.items():
            if count > 0:
                report.write(f"{category}: {count}\n")
        report.write(f"\nTotal: {total}\n")
        if unknown_errors:
            report.write("\nUNKNOWN ERRORS FOUND:\n")
            for e in unknown_errors:
                report.write(f"  - {e}\n")
    print(f"\n✅ Report saved to {filename}")    

# ============================================
# MAIN SCRIPT — clean and readable!
# ============================================

# Step 1: Load the file
lines = load_log_file("bot_logs.txt")

# Step 2: Process each line
results         = []
unknown_errors  = []
category_counts = {
    "🌐 Network Issue"  : 0,
    "🔐 Auth Issue"     : 0,
    "📂 Data Issue"     : 0,
    "⚙️  System Issue"  : 0,
    "❓ Unknown"        : 0,
}

for line in lines:
    bot_name, timestamp, error = parse_log_line(line)
    category                   = clasify_error(error)

    category_counts[category] = +1
    results.append((bot_name, error, category))

    if category == "❓ Unknown" and error not in unknown_errors:
        unknown_errors.append(error)

# Step 3: Display results
print_results(results)

# Step 4: Show summary
print_summary(category_counts, len(lines))

# Step 5: Alert unknowns
if unknown_errors:
    print()
    print("⚠️  UNKNOWN ERROR TYPES DETECTED:")
    for unknown in unknown_errors:
        print(f"   → '{unknown}'")

# Step 6: Save report
save_report("classification_report_v3.txt", category_counts, unknown_errors, len(lines))