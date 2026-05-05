class BotNotFoundError(Exception):
    """Raised when a bot is not found in the fleet."""
    pass

class FleetEmptyError(Exception):
    """Raised when an operation is attempted on an empty fleet."""
    pass