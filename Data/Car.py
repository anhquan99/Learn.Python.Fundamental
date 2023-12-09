import re
from Exception.InputException import InputException

class Car:
    def __init__(self, identity: str, available_credit = 0):
        self.identity = identity
        self.available_credit = available_credit

    @property
    def identity(self):
        return self._identity
    @property
    def available_credit(self):
        return self._available_credit
    @available_credit.setter
    def available_credit(self, available_credit):
        if available_credit < 0:
            raise InputException("Available Credit")
        self._available_credit = available_credit
