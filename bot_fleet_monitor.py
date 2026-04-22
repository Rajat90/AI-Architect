import os
from datetime import datetime

# ── DATA ──────────────────────────────────────────────────────────────
bot_fleet = [
    {"bot_id": "BOT_001", "queue": "AP_Invoices",   "status": "Running", "processed": 42, "errors": 1},
    {"bot_id": "BOT_002", "queue": "HR_Onboarding", "status": "Failed",  "processed": 18, "errors": 5},
    {"bot_id": "BOT_003", "queue": "AP_Invoices",   "status": "Idle",    "processed": 67, "errors": 0},
    {"bot_id": "BOT_004", "queue": "Finance_Recon", "status": "Running", "processed": 31, "errors": 2},
]

# ── FUNCTIONS ─────────────────────────────────────────────────────────
def get_error_rate(bot):
    if bot["processed"] == 0:
        return 0.0
    return bot["errors"] / bot["processed"] * 100

def get_health(bot):
    return "Critical" if bot["errors"] >= 3 else "OK"

def get_critical_bots(fleet):
    return [bot for bot in fleet if bot["errors"] >= 3]

def get_best_bot(fleet):
    return max(fleet, key=lambda bot: bot["processed"])

def filter_by_queue(fleet, queue_name):
    return [bot for bot in fleet if bot["queue"] == queue_name]

def get_fleet_summary(fleet):
    return {
        "total_bots":      len(fleet),
        "total_processed": sum(bot["processed"] for bot in fleet),
        "critical_count":  len(get_critical_bots(fleet))
    }

def build_report(fleet):
    return [
        {
            "bot_id":     bot["bot_id"],
            "queue":      bot["queue"],
            "status":     bot["status"],
            "error_rate": f"{get_error_rate(bot):.1f}%",
            "health":     get_health(bot)
        }
        for bot in fleet
    ]

# ── FILE OUTPUT ───────────────────────────────────────────────────────
def save_report(fleet):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/fleet_report_{timestamp}.txt"

    report = build_report(fleet)
    summary = get_fleet_summary(fleet)

    with open(filename, "w") as f:
        f.write("BOT FLEET MONITOR REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")

        for row in report:
            f.write(f"{row['bot_id']} | {row['queue']} | {row['status']} | "
                    f"Error Rate: {row['error_rate']} | Health: {row['health']}\n")

        f.write("\n" + "=" * 50 + "\n")
        f.write(f"Total Bots:      {summary['total_bots']}\n")
        f.write(f"Total Processed: {summary['total_processed']}\n")
        f.write(f"Critical Bots:   {summary['critical_count']}\n")

    print(f"Report saved: {filename}")

# ── MENU ──────────────────────────────────────────────────────────────
def show_menu():
    print("\n" + "=" * 40)
    print("  BOT FLEET MONITOR")
    print("=" * 40)
    print("1. Full fleet report")
    print("2. Critical bots only")
    print("3. Filter by queue")
    print("4. Fleet summary")
    print("5. Best performing bot")
    print("6. Save report to file")
    print("0. Exit")
    print("=" * 40)

def run_monitor():
    print("\n" + "Bot Fleet Monitor v1 — starting...")

    while True:
        show_menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            report = build_report(bot_fleet)
            print()
            for row in report:
                print(f"{row['bot_id']} | {row['queue']} | {row['status']} | "
                      f"Error Rate: {row['error_rate']} | Health: {row['health']}")

        elif choice == "2":
            critical = get_critical_bots(bot_fleet)
            print(f"\nCritical bots ({len(critical)}):")
            for bot in critical:
                print(f"  {bot['bot_id']} — {bot['errors']} errors")

        elif choice == "3":
            queue = input("Enter queue name: ").strip()
            results = filter_by_queue(bot_fleet, queue)
            if results:
                for bot in results:
                    print(f"  {bot['bot_id']} | {bot['status']} | {bot['processed']} processed")
            else:
                print(f"No bots found on queue: {queue}")

        elif choice == "4":
            summary = get_fleet_summary(bot_fleet)
            print(f"\nTotal Bots:      {summary['total_bots']}")
            print(f"Total Processed: {summary['total_processed']}")
            print(f"Critical Bots:   {summary['critical_count']}")

        elif choice == "5":
            best = get_best_bot(bot_fleet)
            print(f"\nBest bot: {best['bot_id']} — {best['processed']} processed")

        elif choice == "6":
            save_report(bot_fleet)

        elif choice == "0":
            print("Shutting down monitor. Goodbye.")
            break

        else:
            print("Invalid option. Try again.")

# ── ENTRY POINT ───────────────────────────────────────────────────────
if __name__ == "__main__":
    run_monitor()