import re
import functools
from Exception.InputException import InputException

def validate_date(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if not re.match("^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", val):
            raise InputException("Date")
        return val
    return wrapper
