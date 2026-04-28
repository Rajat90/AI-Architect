class FleetMonitorError(Exception):
    """Base class for exceptions in this module."""
    pass

class BotDataError(FleetMonitorError):  
#accepts: message, bot_name=None
    def __init__(self, message, bot_name=None):
        self.message = message
        self.bot_name = bot_name
        super().__init__(self.message)

class FleetThresholdError(FleetMonitorError):  # threshold breach
#accepts: message, bot_name=None, threshold=None, actual=None
    def __init__(self, message, bot_name=None, threshold=None, actual=None):
        self.message = message
        self.bot_name = bot_name
        self.threshold = threshold
        self.actual = actual
        super().__init__(self.message)
    

class ReportError(FleetMonitorError):       # save/build failures
#accepts: message, filename=None
    def __init__(self, message, filename=None):        
        self.message = message
        self.filename = filename
        super().__init__(self.message)


#Then write a test function: validate_bot(bot)
#Raises BotDataError if:
#   - "name" key missing
#   - "error_count" key missing  
#   - "tasks_completed" value is 0 (can't divide later)
def validate_bot(bot):
    if "name" not in bot:
        raise BotDataError("Bot data is missing the 'name' key.", bot_name="UNKNOWN")
    
    if "error_count" not in bot:
        raise BotDataError("Bot data is missing the 'error_count' key.", bot_name=bot.get("name"))
    
    if "tasks_completed" not in bot:
        raise BotDataError("Missing 'tasks_completed' key.", bot_name=bot.get("name"))

    if bot["tasks_completed"] == 0:
        raise BotDataError("Zero tasks completed — division undefined.", bot_name=bot["name"])