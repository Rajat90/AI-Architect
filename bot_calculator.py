# ================================
# Bot Performance Calculator
# ================================

# Ask the user for information
department = input("Enter department name: ")
bot_name = input("Enter bot name: ")
total_runs = int(input("Enter total runs: "))
total_failures = int(input("Enter total failures: "))

# Calculate success rate
success_rate = (total_runs - total_failures) / total_runs * 100

# Calculate total successful runs
successful_runs = total_runs - total_failures

# Decide the health status based on success rate
if success_rate >= 95:
    health = "🟢 HEALTHY"
elif success_rate >= 80:
    health = "🟡 WARNING"
else:
    health = "🔴 CRITICAL"

# Generate a recommendation
if health == "🔴 CRITICAL":
    recommendation = "URGENT: Investigate and fix immediately"
elif health == "🟡 WARNING":
    recommendation = "REVIEW: Schedule a check this week"
else:
    recommendation = "MONITOR: Continue normal operations"    

# Print the result
print()
print("=" * 45)
print("       BOT PERFORMANCE REPORT")
print("=" * 45)
print(f"  Bot Name     : {bot_name}")
print(f"  Department   : {department}")
print(f"  Total Runs   : {total_runs}")
print(f"  Failures     : {total_failures}")
print(f"  Successful   : {successful_runs}")
print(f"  Success Rate : {success_rate:.2f}%")
print(f"  Health       : {health}")
print(f"  Action       : {recommendation}")
print("=" * 45)
print()