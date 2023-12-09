import re
import functools
from Exception.InputException import InputException

class CarIdValidation(object):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        val = self.func(*args, **kwargs)
        print(**kwargs)
        # if not re.match("^[a-zA-Z]{3}-\\d{5}$", val):
        #     raise InputException("Car Identity")