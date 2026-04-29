# monitor.py
import os
from datetime import datetime
from config import OUTPUT_DIR, REPORT_FILENAME_PREFIX
from exceptions import ReportError
from utils import get_error_rate, get_health, get_fleet_summary

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

def save_report(fleet):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/{REPORT_FILENAME_PREFIX}_{timestamp}.txt"

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
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

    except OSError as e:
        raise ReportError(f"Failed to save report: {e}", filename=filename)
    else:
        print(f"Report saved: {filename}")
    finally:
        print("Save attempt complete")