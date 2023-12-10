
class ParkingTicket:
    def __init__(self, arrive_time, fqn: str):
        self.arrive_time = arrive_time
        if fqn is None:
            fqn = ""
        self.fqn = fqn
        self.is_valid_fqn = self.check_valid_fqn(fqn)
        self.exist_time = None
        self.price = None

    def check_valid_fqn(self, fqn):
        modulo_number = 11
        sum = 0
        for i in range(len(fqn)):
            sum += int(fqn[i]) * (i + 1)
        return sum == 0 and sum % modulo_number == 0
    @property
    def fqn(self):
        return self._fqn
    @fqn.setter
    def fqn(self, fqn):
        self._fqn = fqn
        self.is_valid_fqn = self.check_valid_fqn(fqn)