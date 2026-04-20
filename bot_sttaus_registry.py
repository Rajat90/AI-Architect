# Bot Status Registry
# Tracks live state of a single bot — like RE Framework's InitAllApplications + transaction state

bot_state = {
    "bot_id": "BOT_001",
    "queue": "AP_Invoices",
    "status": "Running",
    "current_txn": "TXN004",
    "retries": 0,
    "last_error": None,
    "processed_txns"  : 4,
    "success_rate" : 0
}

bot_state["success_rate"] = bot_state["processed_txns"] / 5 * 100


print (f"Processed:  {bot_state["processed_txns"]}")
print (f"Sucess Rate:  {bot_state["success_rate"]:.1f}%")

# # Simulate a SystemException
# bot_state["status"] = "Failed"
# bot_state["retries"] += 1
# bot_state["last_error"] = "SystemException: SAP timeout"



# # Decision logic — RE Framework retry check
# if bot_state["retries"] < 3:
#     bot_state["status"] = "Retrying"
#     print(f"Retrying {bot_state['current_txn']} — attempt {bot_state['retries']}")
# else:
#     bot_state["status"] = "Abandoned"
#     print(f"TXN abandoned after {bot_state['retries']} retries")

# # Print full state
# print("\nBot State Snapshot:")
# for key, value in bot_state.items():
#     print(f"  {key}: {value}")