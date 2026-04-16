# ================================
# Dictionary Practice
# ================================

# Create a dictionary of bot statuses
bot_statuses = {
    "Vertrag"    : "Running",
    "InvoiceBot" : "Failed",
    "HRBot"      : "Idle",
    "FinanceBot" : "Running",
    "EmailBot"   : "Failed"
}

# Access individual values
print(bot_statuses["Vertrag"])     # Running
print(bot_statuses["InvoiceBot"])  # Failed

# Add a new bot
bot_statuses["PayrollBot"] = "Running"

# Update an existing bot
bot_statuses["HRBot"] = "Running"

# Count total bots
print(f"Total bots tracked: {len(bot_statuses)}")

# Loop through all bots
print()
print("=" * 35)
print("ALL BOT STATUSES:")
print("=" * 35)

for bot_name, status in bot_statuses.items():
    print(f"  {bot_name:<15} : {status}")

# While loop — retry simulation
print()
print("=" * 35)
print("BOT RESTART SIMULATION:")
print("=" * 35)

max_retries = 3
attempt = 0
bot_name = "InvoiceBot"

while attempt < max_retries:
    attempt += 1
    print(f"  Attempt {attempt}: Trying to restart {bot_name}...")
    
    if attempt == 3:
        print(f"  ✅ {bot_name} restarted successfully!")
    else:
        print(f"  ❌ Attempt {attempt} failed. Retrying...")

print(f"  Total attempts needed: {attempt}")