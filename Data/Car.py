import re
from Exception.InputException import InputException

class Car:
    def __init__(self, identity: str, fqn: str, available_credit = 0):
        self.identity = identity
        self.fqn = fqn
        self.available_credit = available_credit

    @property
    def identity(self):
        return self._identity
    @identity.setter
    def identity(self, identity: str):
        if not re.match("^[a-zA-Z]{3}-\\d{5}$", identity):
            raise InputException("Identity")
        self._identity = identity
        
    @property
    def available_credit(self):
        return self._available_credit
    @available_credit.setter
    def available_credit(self, available_credit):
        if available_credit < 0:
            raise InputException("Available Credit")
        self._available_credit = available_credit

    @property
    def fqn(self):
        return self._fqn
    @fqn.setter
    def fqn(self, fqn: str):
        self._fqn = fqn