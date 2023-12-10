import re
from Exception.InputException import InputException

class Car:
    def __init__(self, identity: str, available_credit = 0):
        self.identity = identity
        self.available_credit = available_credit
        self.parking_tickets = []
    @property
    def available_credit(self):
        return self._available_credit
    @available_credit.setter
    def available_credit(self, available_credit):
        if available_credit < 0:
            raise InputException("Available Credit")
        self._available_credit = available_credit
    def is_parking(self):
        return filter(lambda x: x.exist_time is None, self.parking_tickets) is not None
    def get_current_parking_ticket(self):
        return next((x for x in self.parking_tickets if x.exist_time is None), None)