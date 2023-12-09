
class ParkingTicket:
    def __init__(self, car_id, arrive_time, fqn: str):
        self.car_id = car_id
        self.arrive_time = arrive_time
        self.fqn = fqn
        
    def __init__(self, car_id: str, arrive_time, fqn: str, exist_time, price):
        self.car_id = car_id
        self.arrive_time = arrive_time
        self.exist_time = exist_time
        self.price = price
        self.fqn = fqn
    
    def check_valid_fqn(self, fqn):
        modulo_number = 7
        sum = 0
        for i in range(len(fqn)):
            sum += int(fqn[i]) * (i + 1)
        return sum == 0 and sum % modulo_number == 0