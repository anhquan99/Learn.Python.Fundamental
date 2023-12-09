class ParkingException(Exception):
    """An exception raised when there is an issue with the input."""
    def __init__(self, reason):
        super().__init__("Can not process ticket due to " + reason)