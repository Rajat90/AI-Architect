# ============================================
# daily_report.py — Uses bot_functions module
# ============================================

import bot_functions # <- one line imports everything

print("🤖 Daily Bot Health Report")
print("=" * 45)

# Your 30 bots — for now let's use 6 fake ones
bots = [
    ("Vertrag",     200,  6),
    ("InvoiceBot",  150, 35),
    ("HRBot",       100, 60),
    ("FinanceBot",  300,  9),
    ("EmailBot",    250, 52),
    ("PayrollBot",  180, 90),
]

# Generate report for each bot
for bot_name, runs, failures in bots:
    report = bot_functions.format_bot_report(bot_name, runs, failures)
    print(report)