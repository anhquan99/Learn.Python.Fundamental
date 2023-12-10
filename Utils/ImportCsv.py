import csv
import re
import datetime as dt
from Data.ParkDay import ParkDay, ParkHour

class ImportParkingPriceList:

    time_range_pattern = "(\d{2}:\d{2}|Midnight) - (\d{2}:\d{2}|Midnight)"
    
    def __init__(self):
        self.time_ranges = []
        self.mapping_dow = {
            'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6
        }
        self.ParkDays = []

    def import_parking_price_list(self, csv_file):
        with open(csv_file) as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                i += 1
                if i == 2:
                    self.handle_time_ranges(row)
                    if len(self.time_ranges) == 0:
                        raise Exception("Invalid time range format")
                if i > 3:
                    self.handle_time_span(row)
            f.close()
        return tuple(self.ParkDays)

    def handle_time_ranges(self, arr):
        for i in range(len(arr)):
            matchResult = re.search(self.time_range_pattern, arr[i])
            if matchResult:
                time = matchResult.group(0).replace(' ', '').split('-')
                if(time[0] == 'Midnight'):
                    start_time = dt.time.fromisoformat('00:00:00')
                else:
                    start_time = dt.time.fromisoformat(time[0])
                if time[1] == 'Midnight':
                    end_time = dt.time.fromisoformat('23:59:59')
                else:
                    end_time = dt.time.fromisoformat(time[1])
                self.time_ranges.append(TimeRange(start_time, end_time, i, i+1))
    def handle_time_span(self, arr):
        day = self.mapping_dow[arr[0]]
        park_day = ParkDay(day)
        self.ParkDays.append(park_day)
        for i in range(len(self.time_ranges)):
            park_day.park_hours.append(ParkHour(self.time_ranges[i].start_time, self.time_ranges[i].end_time, arr[self.time_ranges[i].max_stay_index], arr[self.time_ranges[i].price_per_hour_index]))

class TimeRange:
    def __init__(self, start_time, end_time, max_stay_index, price_per_hour_index):
        self.start_time = start_time
        self.end_time = end_time
        self.max_stay_index = max_stay_index
        self.price_per_hour_index = price_per_hour_index