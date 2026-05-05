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

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "retries": self.retries
        }

    def __str__(self):
        health = "healthy" if self.is_healthy() else "at risk"
        return f"{self.name} | {self.status} | retries: {self.retries} | {health}"


class AttendedBot(Bot):
    def __init__(self, name, status, user, retries=0):
        super().__init__(name, status, retries)
        self.user = user

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "attended"
        data["user"] = self.user
        return data

    def __str__(self):
        return f"{super().__str__()} | user: {self.user}"


class UnattendedBot(Bot):
    def __init__(self, name, status, schedule, retries=0):
        super().__init__(name, status, retries)
        self.schedule = schedule

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "unattended"
        data["schedule"] = self.schedule
        return data

    def __str__(self):
        return f"{super().__str__()} | schedule: {self.schedule}"