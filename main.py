# main.py
from exceptions import BotDataError, FleetThresholdError, ReportError
from utils import validate_bot, get_critical_bots, filter_by_queue, get_best_bot, get_fleet_summary, check_threshold
from monitor import build_report, save_report

bot_fleet = [
    {"bot_id": "BOT_001", "queue": "AP_Invoices",   "status": "Running", "processed": 42, "errors": 1},
    {"bot_id": "BOT_002", "queue": "HR_Onboarding", "status": "Failed",  "processed": 18, "errors": 5},
    {"bot_id": "BOT_003", "queue": "AP_Invoices",   "status": "Idle",    "processed": 67, "errors": 0},
    {"bot_id": "BOT_004", "queue": "Finance_Recon", "status": "Running", "processed": 31, "errors": 2},
]

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
    print("7. Live threshold scan")
    print("0. Exit")
    print("=" * 40)

def run_monitor():
    print("\nBot Fleet Monitor v2 — starting...")

    for bot in bot_fleet:
        try:
            validate_bot(bot)
        except BotDataError as e:
            print(f"[STARTUP WARNING] Invalid bot data — {e.bot_name}: {e}")

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
            try:
                save_report(bot_fleet)
            except ReportError as e:
                print(f"[ERROR] Could not save report: {e}")

        elif choice == "7":
            print("\nTHRESHOLD SCAN")
            print("-" * 40)
            breach_count = 0
            for bot in bot_fleet:
                try:
                    check_threshold(bot)
                except FleetThresholdError as e:
                    print(f"  [BREACH] {e.bot_name} | Rate: {e.actual}% | Threshold: {e.threshold}%")
                    breach_count += 1
                else:
                    print(f"  {bot['bot_id']} OK")
            print(f"\nTotal breach count: {breach_count}")

        elif choice == "0":
            print("Shutting down monitor. Goodbye.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run_monitor()