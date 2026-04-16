# ================================
# Bot Status Report — Vertrag Bot
# ================================

# Bot Information
department = "Finance"
bot_name = "Vertrag"
status = "Running"
last_run = "2024-01-15"

# Performance Numbers
total_runs = 200
total_failures = 6

# Python calculates the success rate for us
success_rate = (total_runs - total_failures) / total_runs * 100

# Now print a nice report
print("================================")
print("BOT STATUS REPORT")
print("================================")
print("Department Name: " + department)
print("Bot Name  : " + bot_name)
print("Status    : " + status)
print("Last Run  : " + last_run)
print("Total Runs: " + str(total_runs))
print("Failures  : " + str(total_failures))
print("Success % : " + str(success_rate))
print("================================")

