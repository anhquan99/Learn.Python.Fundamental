import re
import functools
from Exception.InputException import InputException

class DateValidation:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        val = self.func(*args, **kwds)
        if not re.match("^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$", val):
            raise InputException("Date")
