
class ParkDay:
    def __init__(self, park_hours : str):
        self.park_hours = park_hours

class ParkHour:
    def __init__(self, start_time, end_time, max_stay_hours, price_per_hour):
        self.start_time = start_time
        self.end_time = end_time
        self.max_stay_hours = max_stay_hours
        self.price_per_hour = price_per_hour