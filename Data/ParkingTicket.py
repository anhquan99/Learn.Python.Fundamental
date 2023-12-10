
class ParkingTicket:
    def __init__(self, arrive_time, fqn: str):
        self.arrive_time = arrive_time
        self.fqn = fqn
        self.is_valid_fqn = self.check_valid_fqn(fqn)
        self.exist_time = None
        
    # def __init__(self, arrive_time, fqn: str, exist_time, price):
    #     self.arrive_time = arrive_time
    #     self.exist_time = exist_time
    #     self.price = price
    #     self.fqn = fqn
    #     self.is_valid_fqn = check_valid_fqn(fqn)
    
    def check_valid_fqn(self, fqn):
        modulo_number = 7
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