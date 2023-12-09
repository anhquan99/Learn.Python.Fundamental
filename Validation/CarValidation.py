import re
import functools
from Exception.InputException import InputException

class CarIdValidation:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        val = self.func(*args, **kwds)
        if not re.match("^[a-zA-Z]{3}-\\d{5}$", val):
            raise InputException("Car Identity")