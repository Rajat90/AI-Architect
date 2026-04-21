# Multi-Bot Report Parser
# Equivalent to RE Framework end-of-run reporting

bot_fleet = [
    {"bot_id": "BOT_001", "queue": "AP_Invoices",   "status": "Running", "processed": 42, "errors": 1},
    {"bot_id": "BOT_002", "queue": "HR_Onboarding", "status": "Failed",  "processed": 18, "errors": 5},
    {"bot_id": "BOT_003", "queue": "AP_Invoices",   "status": "Idle",    "processed": 67, "errors": 0},
    {"bot_id": "BOT_004", "queue": "Finance_Recon", "status": "Running", "processed": 31, "errors": 2},
]


# 1. find best performing bot (most processed)
# You need the full record to get bot_id
best_bot = max(bot_fleet, key=lambda bot: bot["processed"])
print(f"Best bot: {best_bot['bot_id']} — {best_bot['processed']} processed")


# 2. AP invoice queue report
# Cleaner — list of dicts, consistent with the fleet pattern
AP_queue_bots = [
    {"bot_id": bot["bot_id"], "processed": bot["processed"]}
    for bot in bot_fleet if bot["queue"] == "AP_Invoices"
]
for bot in AP_queue_bots:
    print(f"{bot['bot_id']} processed {bot['processed']} items in AP_Invoices queue.")




# 3. Add health key to each bot
for bot in bot_fleet:
   if bot["errors"] < 3:
       bot["health"] = "ok"
   else:
       bot["health"] = "critical"
print("Bot fleet with health status:")
for bot in bot_fleet:
    print(f"{bot['bot_id']} — health: {bot['health']}")

# 1. Filter — only failed bots
failed = [bot for bot in bot_fleet if bot["status"] == "Failed"]
print(f"Failed bots: {len(failed)}")

# 2. Aggregate — total processed across fleet
total_processed = sum(bot["processed"] for bot in bot_fleet)
print(f"Total processed: {total_processed}")

# 3. Transform — build summary report
report = [
    {
        "bot_id": bot["bot_id"],
        "error_rate": f"{bot['errors'] / bot['processed'] * 100:.1f}%"
    }
    for bot in bot_fleet
]

for row in report:
    print(f"{row['bot_id']} — error rate: {row['error_rate']}")

