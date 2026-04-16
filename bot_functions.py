# ============================================
# bot_functions.py — Reusable Bot Automation Library
# ============================================


def calculate_success_rate(total_runs, total_failures):
    """Calculates success rate percentage for a bot."""
    if total_runs == 0:
        return 0
    successful = total_runs - total_failures
    rate = (successful / total_runs) * 100
    return rate


def get_health_status(success_rate):
    """Returns health label based on success rate."""
    if success_rate >= 95:
        return "🟢 HEALTHY"
    elif success_rate >= 80:
        return "🟡 WARNING"
    else:
        return "🔴 CRITICAL"


def get_recommendation(health_status):
    """Returns action recommendation based on health status."""
    if health_status == "🔴 CRITICAL":
        return "URGENT: Investigate immediately"
    elif health_status == "🟡 WARNING":
        return "REVIEW: Schedule check this week"
    else:
        return "MONITOR: Continue normal operations"


def classify_error(error_text):
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
    return "❓ Unknown"


def format_bot_report(bot_name, runs, failures):
    """Generates a complete formatted report string for one bot."""
    rate   = calculate_success_rate(runs, failures)
    health = get_health_status(rate)
    action = get_recommendation(health)

    report = f"""
{'=' * 45}
  BOT REPORT: {bot_name}
{'=' * 45}
  Runs       : {runs}
  Failures   : {failures}
  Rate       : {rate:.2f}%
  Health     : {health}
  Action     : {action}
{'=' * 45}"""
    return report


# ============================================
# This block ONLY runs when you execute this
# file directly — NOT when it's imported
# ============================================

if __name__ == "__main__":
    print("🧪 Testing bot_functions module...")
    print("=" * 45)
    
    # Test calculate_success_rate
    rate = calculate_success_rate(200, 6)
    print(f"✅ calculate_success_rate(200, 6) = {rate:.2f}%")
    
    # Test get_health_status
    health = get_health_status(rate)
    print(f"✅ get_health_status({rate:.2f}) = {health}")
    
    # Test get_recommendation
    action = get_recommendation(health)
    print(f"✅ get_recommendation({health}) = {action}")
    
    # Test classify_error
    test_errors = ["Timeout", "Login Failed", "Unknown Error"]
    for error in test_errors:
        category = classify_error(error)
        print(f"✅ classify_error('{error}') = {category}")
    
    # Test format_bot_report
    print(format_bot_report("TestBot", 200, 6))
    
    print("All tests passed! ✅")