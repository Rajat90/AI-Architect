# utils.py
from config import CRITICAL_ERROR_THRESHOLD, CRITICAL_ERROR_RATE
from exceptions import BotDataError, FleetThresholdError

def validate_bot(bot):
    if "bot_id" not in bot:
        raise BotDataError("Missing 'bot_id' key.", bot_name="UNKNOWN")
    if "errors" not in bot:
        raise BotDataError("Missing 'errors' key.", bot_name=bot["bot_id"])
    if "processed" not in bot:
        raise BotDataError("Missing 'processed' key.", bot_name=bot["bot_id"])

def get_error_rate(bot):
    if bot["processed"] == 0:
        return 0.0
    return bot["errors"] / bot["processed"] * 100

def get_health(bot):
    return "Critical" if bot["errors"] >= CRITICAL_ERROR_THRESHOLD else "OK"

def get_critical_bots(fleet):
    return [bot for bot in fleet if bot["errors"] >= CRITICAL_ERROR_THRESHOLD]

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


# Requirements:
# - calculate error rate using get_error_rate()
# - if error rate > CRITICAL_ERROR_RATE:
#       raise FleetThresholdError with:
#           message: clear description
#           bot_name: bot's bot_id
#           threshold: CRITICAL_ERROR_RATE
#           actual: the calculated error rate (rounded to 1 decimal)
# - if below threshold: return None (clean pass)
def check_threshold(bot):
    error_rate = get_error_rate(bot)
    if error_rate >= CRITICAL_ERROR_RATE:
        raise FleetThresholdError(
            message=f"Bot {bot['bot_id']} exceeded critical error rate threshold.",
            bot_name=bot['bot_id'],
            threshold=CRITICAL_ERROR_RATE,
            actual=round(error_rate, 1)
        )
    return None