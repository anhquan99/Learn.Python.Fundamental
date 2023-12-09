class CarException(Exception):
    """An exception raised when there is an issue with the input."""
    def __init__(self, reason):
        super().__init__("Car is not available because of:  " + reason)
