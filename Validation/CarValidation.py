import re
import functools
from Exception.InputException import InputException

def car_id_validation(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if not re.match("^[0-9a-zA-Z]{3}-\\d{5}$", val):
            raise InputException("Car Identity")
        return val
    return wrapper
def validate_number(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if not re.match("^\\d+$", val):
            raise InputException("Number")
        return val
    return wrapper