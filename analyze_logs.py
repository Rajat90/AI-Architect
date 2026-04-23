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


def analyze_logs (bot_logs):
# Extract falied results
    failed_results = [res for res in bot_logs if res["status"] == "FAILED"]
    
# From failed_results, build a new list called failed_bots containing only the bot names
    failed_bots = [res["bot"] for res in failed_results]
    

# Now build a dictionary called fail_count
    failed_count = {bot: failed_bots.count(bot) for bot in failed_bots}
    return failed_count

def print_failed_count(failed_count):
    print(f"=== Bot Failure Summary ===")
    for bot, count in failed_count.items():
        print(f"{bot:<15}: {count} failures")
    print("="*30)

if __name__ == "__main__":
    failed_count = analyze_logs(bot_logs)
    print_failed_count(failed_count)    