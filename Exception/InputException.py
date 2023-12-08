class InputException(Exception):
    """An exception raised when there is an issue with the input."""
    def __init__(self, field_name):
        super().__init__("Invalid " + field_name)
