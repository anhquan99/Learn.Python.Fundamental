
class ParkingTicket:
    def __init__(self, car_id, arrive_time):
        self.car_id = car_id
        self.arrive_time = arrive_time
    def __init__(self, car_id, arrive_time, exist_time, price):
        self.car_id = car_id
        self.arrive_time = arrive_time
        self.exist_time = exist_time
        self.price = price