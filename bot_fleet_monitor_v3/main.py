from models.bot import Bot, AttendedBot, UnattendedBot
from models.fleet import Fleet
from exceptions import BotNotFoundError, FleetEmptyError

fleet = Fleet()
fleet.add_bot(AttendedBot("Invoice-Bot", "running", user="rajat"))
fleet.add_bot(UnattendedBot("PO-Bot", "failed", schedule="daily-02:00", retries=3))
fleet.add_bot(Bot("GL-Bot", "running"))

for bot in fleet.bots:
    print(bot)

print()
print(fleet.summary())

print()
try:
    bot = fleet.get_bot("HR-Bot")
except BotNotFoundError as e:
    print(f"Error: {e}")