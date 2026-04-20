# Fleet registry — multiple bots, each bot is a dict
fleet = {
    "BOT_001": {"queue": "AP_Invoices", "status": "Running", "retries": 0},
    "BOT_002": {"queue": "HR_Onboarding", "status": "Failed", "retries": 2},
    "BOT_003": {"queue": "AP_Invoices", "status": "Idle", "retries": 0},
    "BOT_004": {"queue": "Finance_Recon", "status": "Running", "retries": 0},
}

# Access nested value
print(fleet["BOT_003"]["status"])        # Idle

# Update nested value
fleet["BOT_002"]["retries"] += 1
fleet["BOT_002"]["status"] = "Abandoned"

# Print Failed Bot
failed_map = {name: stati["status"] for name, stati in fleet.items() if stati["status"] not in ["Running", "Idle"]}
print (failed_map)  

# # Iterate fleet
# for bot_id, state in fleet.items():
#     print(f"{bot_id} | {state['queue']} | {state['status']}")