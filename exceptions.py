# exceptions.py
class FleetMonitorError(Exception):
    pass

class BotDataError(FleetMonitorError):
    def __init__(self, message, bot_name=None):
        super().__init__(message)
        self.bot_name = bot_name

class FleetThresholdError(FleetMonitorError):
    def __init__(self, message, bot_name=None, threshold=None, actual=None):
        super().__init__(message)
        self.bot_name = bot_name
        self.threshold = threshold
        self.actual = actual

class ReportError(FleetMonitorError):
    def __init__(self, message, filename=None):
        super().__init__(message)
        self.filename = filename