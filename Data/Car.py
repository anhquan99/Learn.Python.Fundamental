import re
from Exception.InputException import InputException
from Validation.CarValidation import CarIdValidation, FqnValidation

class Car:
    def __init__(self, identity: str, fqn: str, available_credit = 0):
        self.identity = identity
        self.fqn = fqn
        self.available_credit = available_credit
        self.is_valid_fqn = fqn

    @property
    def identity(self):
        return self._identity
    @CarIdValidation
    @identity.setter
    def identity(self, identity: str):
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
    def is_valid_fqn(self):
        return self._is_valid_fqn
    @FqnValidation
    @is_valid_fqn.setter
    def is_valid_fqn(self, fqn):
        self._is_valid_fqn = fqn
    def print(self):
        print(self.identity, self.fqn, self.available_credit, self.is_valid_fqn)