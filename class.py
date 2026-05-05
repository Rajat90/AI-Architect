class Bot:
    def __init__(self, name, status, retries=0):
        self.name = name
        self.status = status
        self.retries = retries

    def is_healthy(self):
        return self.status == "running" and self.retries < 3
    
    def increment_retry(self):
        self.retries += 1

    def marked_failed(self):
        self.status = "failed"

    def describe(self):
        health = "healthy" if self.is_healthy() else "at risk"
        return f"{self.name} | {self.status} | retries: {self.retries} | {health}"
    
# --- Instantiate and test ---
bot1 = Bot("Invoice-Bot", "running")
bot2 = Bot("PO-Bot", "failed", retries=3)

print(bot1.describe())
print(bot2.describe())

bot1.increment_retry()
bot1.increment_retry()
bot1.increment_retry()
print(bot1.describe())  # What changes?

bot1.marked_failed()
print(bot1.describe())  # What changes now?