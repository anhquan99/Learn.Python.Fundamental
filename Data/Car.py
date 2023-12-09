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
    @property
    def packing_tickets(self):
        return self._packing_tickets
    @packing_tickets.getter
    def packing_tickets(self):
        if self.packing_tickets is None:
            self.packing_tickets = []
        return self._packing_tickets
    def is_parking(self):
        return any(lambda x: x.exist_time is None, self.packing_tickets)
    def get_current_packing_ticket(self):
        return next((x for x in self.packing_tickets if x.exist_time is None), None)
