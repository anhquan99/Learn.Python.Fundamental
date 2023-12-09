
class ParkDay:
    def __init__(self, day_of_week):
        self.park_hours = []
        self.day_of_week = day_of_week
    def print(self):
        print(self.day_of_week)
        for i in self.park_hours:
            i.print()

class ParkHour:
    def __init__(self, start_time, end_time, max_stay_hours, price_per_hour):
        self.start_time = start_time
        self.end_time = end_time
        self.max_stay_hours = max_stay_hours
        self.price_per_hour = price_per_hour
    def print(self):
        print(self.start_time, self.end_time, self.max_stay_hours, self.price_per_hour)