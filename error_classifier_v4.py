# ============================================
# Bot Error Classifier V4 — Module Powered
# ============================================

import bot_functions   # ← all our functions live here now


def load_log_file(filename):
    """Reads a log file and returns list of lines."""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"📂 Loaded {len(lines)} entries from {filename}")
    return lines


def parse_log_line(line):
    """Splits one log line into bot_name, timestamp, error."""
    parts     = line.strip().split(" | ")
    bot_name  = parts[0]
    timestamp = parts[1]
    error     = parts[2]
    return bot_name, timestamp, error


# ============================================
# MAIN SCRIPT
# ============================================

if __name__ == "__main__":
    print("🤖 Bot Error Classifier V4")
    print("=" * 65)

    # Load file
    lines = load_log_file("bot_logs.txt")

    # Process
    results         = []
    unknown_errors  = []
    category_counts = {
        "🌐 Network Issue" : 0,
        "🔐 Auth Issue"    : 0,
        "📂 Data Issue"    : 0,
        "⚙️  System Issue"  : 0,
        "❓ Unknown"        : 0,
    }

    for line in lines:
        bot_name, timestamp, error = parse_log_line(line)
        category = bot_functions.classify_error(error)  # ← from module!

        category_counts[category] += 1
        results.append((bot_name, error, category))

        if category == "❓ Unknown" and error not in unknown_errors:
            unknown_errors.append(error)

    # Display results
    print(f"\n{'BOT':<15} {'ERROR':<25} {'CATEGORY'}")
    print("-" * 65)
    for bot_name, error, category in results:
        print(f"{bot_name:<15} {error:<25} {category}")
    print("=" * 65)

    # Summary
    print("\n📊 SUMMARY")
    print("=" * 40)
    for category, count in category_counts.items():
        if count > 0:
            bar = "█" * count
            print(f"  {category:<22}: {count:>3}  {bar}")

    # Unknowns alert
    if unknown_errors:
        print("\n⚠️  UNKNOWN ERRORS:")
        for e in unknown_errors:
            print(f"   → '{e}'")
    else:
        print("\n✅ All errors classified!")