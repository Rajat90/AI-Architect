from models.bot import Bot
from exceptions import BotNotFoundError, FleetEmptyError


class Fleet:
    def __init__(self):
        self.bots = []

    def add_bot(self, bot):
        self.bots.append(bot)

    def get_bot(self, name):
        for bot in self.bots:
            if bot.name == name:
                return bot
        raise BotNotFoundError(f"Bot '{name}' not found in fleet.")

    def get_healthy_count(self):
        return sum(1 for bot in self.bots if bot.is_healthy())

    def get_failed_bots(self):
        return [bot for bot in self.bots if bot.status == "failed"]

    def summary(self):
        if not self.bots:
            raise FleetEmptyError("Cannot summarize an empty fleet.")
        total = len(self.bots)
        healthy = self.get_healthy_count()
        failed = len(self.get_failed_bots())
        return (
            f"Fleet Summary\n"
            f"  Total  : {total}\n"
            f"  Healthy: {healthy}\n"
            f"  Failed : {failed}"
        )