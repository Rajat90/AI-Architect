class Bot:
    max_retries = 3

    def __init__(self, name, status, retries=0):
        self.name = name
        self.status = status
        self.retries = retries

    def is_healthy(self):
        return self.status == "running" and self.retries < Bot.max_retries

    def increment_retry(self):
        self.retries += 1

    def mark_failed(self):
        self.status = "failed"

    def __str__(self):
        health = "healthy" if self.is_healthy() else "at risk"
        return f"{self.name} | {self.status} | retries: {self.retries} | {health}"


class Fleet:
    def __init__(self):
        self.bots = []

    def add_bot(self, bot):
        self.bots.append(bot)

    def get_healthy_count(self):
        # return sum(1 for bot in self.bots if bot.is_healthy())
        count = 0
        for bot in self.bots:
                if bot.is_healthy():
                    count += 1
        return count

    def get_failed_bots(self):
        return [bot for bot in self.bots if bot.status == "failed"]

    def summary(self):
        total = len(self.bots)
        healthy = self.get_healthy_count()
        failed = len(self.get_failed_bots())
        return (
            f"Fleet Summary\n"
            f"  Total  : {total}\n"
            f"  Healthy: {healthy}\n"
            f"  Failed : {failed}"
        )


# --- Build the fleet ---
fleet = Fleet()
fleet.add_bot(Bot("Invoice-Bot", "running"))
fleet.add_bot(Bot("PO-Bot", "failed", retries=3))
fleet.add_bot(Bot("HR-Bot", "running", retries=2))
fleet.add_bot(Bot("GL-Bot", "running"))

# --- Print each bot ---
for bot in fleet.bots:
    print(bot)

print()
print(fleet.summary())

# --- Simulate failures ---
fleet.bots[2].increment_retry()  # HR-Bot hits max
fleet.bots[2].mark_failed()

print()
print("After HR-Bot failure:")
print(fleet.summary())