# Bot Log Analyzer — Week 4 Day 1
# Data: list of bot run logs (your "queue items" from UiPath world)

bot_logs = [
    {"bot": "Invoice_Bot", "status": "FAILED", "error": "FileNotFoundError"},
    {"bot": "HR_Bot", "status": "SUCCESS", "error": None},
    {"bot": "Invoice_Bot", "status": "FAILED", "error": "ValueError"},
    {"bot": "Payroll_Bot", "status": "SUCCESS", "error": None},
    {"bot": "HR_Bot", "status": "FAILED", "error": "TimeoutError"},
    {"bot": "Invoice_Bot", "status": "SUCCESS", "error": None},
    {"bot": "Payroll_Bot", "status": "FAILED", "error": "OSError"},
    {"bot": "HR_Bot", "status": "FAILED", "error": "FileNotFoundError"},
]

# Extract falied results
failed_results = [res for res in bot_logs if res["status"] == "FAILED"]
print(failed_results)

# From failed_results, build a new list called failed_bots containing only the bot names
failed_bots = [res["bot"] for res in failed_results]
print(failed_bots)

# Now build a dictionary called fail_count
failed_count = {bot: failed_bots.count(bot) for bot in failed_bots}
print(failed_count)


# Sort bots by failure count (ascending)
#ranked_bots = sorted(failed_count.items(), key=lambda x: x[1])
ranked_bots = sorted(failed_count.items(), key=lambda x: x[1], reverse=True)
print(ranked_bots)

# find the single bot with the highest failure count from failed_count
worst_offender = max(failed_count.items(), key=lambda x: x[1])
print(f"Worst offender: {worst_offender[0]} with {worst_offender[1]} failures")

#Add a new function rank_bots(failed_count) that:


def rank_bots(failed_count):
    bot_rank = sorted(failed_count.items(), key=lambda x: x[1], reverse=True)
    worst_offender = bot_rank[0]
    print(f"=== Bot Failure Ranking ===")
    #for bot, count in bot_rank:
    #    print(f"{bot}: {count} failures")
    for i, (bot, count) in enumerate(bot_rank, start=1):
        print(f"{i}. {bot:<15}: {count} failures")   
    print()    
    print(f"Worst offender: {worst_offender[0]} with {worst_offender[1]} failures")

if __name__ == "__main__":
    rank_bots(failed_count)
