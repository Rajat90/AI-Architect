
transactions = [
    ("bot_001", "running"),
    ("bot_002", "failed"),
    ("bot_003", "failed")
]

statuses = {bot_id: status for bot_id, status in transactions}
print(statuses)