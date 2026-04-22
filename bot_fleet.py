bot_fleet = [
    {"bot_id": "BOT_001", "queue": "AP_Invoices",   "status": "Running", "processed": 42, "errors": 1},
    {"bot_id": "BOT_002", "queue": "HR_Onboarding", "status": "Failed",  "processed": 18, "errors": 5},
    {"bot_id": "BOT_003", "queue": "AP_Invoices",   "status": "Idle",    "processed": 67, "errors": 0},
    {"bot_id": "BOT_004", "queue": "Finance_Recon", "status": "Running", "processed": 31, "errors": 2},
]

# get Critical Bots returns list of dicts for bots where errors >= 3
def get_critical_bots(fleet):
    return [bot for bot in fleet if bot["errors"] >= 3]

# get_fleet_summary(fleet) — returns a dict with 3 keys:
def get_fleet_summary(fleet):
    total_processed = sum(bot["processed"] for bot in fleet)
    total_bots = len(fleet)
    critical_bots = len(get_critical_bots(fleet))
    return{"total_bots" : total_bots, "total_processed": total_processed, "critical_bots": critical_bots}



def get_error_rate(bot):
    if bot["processed"] == 0:
        return 0.0
    return bot["errors"] / bot["processed"] * 100

def get_health(bot):
    return "Critical" if bot["errors"] >= 3 else "OK"

def get_best_bot(fleet):
    return max(fleet, key=lambda bot: bot["processed"])

def filter_by_queue(fleet, queue_name):
    return [bot for bot in fleet if bot["queue"] == queue_name]

def build_report(fleet):
    report = []
    for bot in fleet:
        report.append({
            "bot_id":     bot["bot_id"],
            "status":     bot["status"],
            "error_rate": f"{get_error_rate(bot):.1f}%",
            "health":     get_health(bot),
            "summary"   : get_fleet_summary(fleet)
        })
    return report

# Run it
report = build_report(bot_fleet)
for row in report:
    print(f"{row['bot_id']} | {row['status']} | {row['error_rate']} | {row['health']}")

best = get_best_bot(bot_fleet)
print(f"\nBest bot: {best['bot_id']} — {best['processed']} processed")

ap_bots = filter_by_queue(bot_fleet, "AP_Invoices")
print(f"\nAP Invoices bots: {[b['bot_id'] for b in ap_bots]}")

summary = get_fleet_summary(bot_fleet)
print(f"\nFleet Summary: Total Bots: {summary['total_bots']} | Total Processed: {summary['total_processed']} | Critical Bots: {summary['critical_bots']}")