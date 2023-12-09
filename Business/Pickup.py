from copy import deepcopy
from Data import Car, ParkDay
from Exception import CarException, ParkingException

class Pickup:
    def __init__(self, cars: [Car], parking_hours: (ParkDay)):
        self.__cars = cars
        self.__picking_up_car = None
        self.__picking_up_ticket = None
        self.__exist_time = None
        self.__parking_hours = parking_hours
    def get_pickup_ticket(self, car_id, exist_time):
        existed_car = next((c for c in self.__cars if c.identity == car_id), None)
        if existed_car is None:
            raise CarException("Car not found.")
        self.__picking_up_car = existed_car
        current_parking_ticket = existed_car.get_current_parking_ticket()
        if current_parking_ticket is None: 
            raise CarException("Car is not parked.")
        self.__picking_up_ticket = current_parking_ticket
        parked_time = exist_time - current_parking_ticket.arrive_time
        if parked_time < 0:
            raise ParkingException.ParkingException("Pick up time can not be before arrive time.")
        self.__exist_time = exist_time
        temporary_ticket = deepcopy(current_parking_ticket)
        temporary_ticket.exist_time = exist_time
        temporary_ticket.price = self.__calculate_price()
        return temporary_ticket
    # TODO: continue implementation
    def __calculate_price(self):
        parked_time = self.__exist_time - self.__picking_up_ticket.arrive_time
        price_on_day, max_stay_hours = self.__get_price_on_day()
        if price_on_day is None:
            raise ParkingException.ParkingException("Some thing wrong with the price list.")
    # TODO: continue implementation
    def __get_price_on_day(self):
        day = self.__picking_up_ticket.arrive_time.day
        arrive_time = self.__picking_up_ticket.arrive_time.time
        price, max_stay_hours = self.__parking_hours.filter(lambda x: x.day_of_week == day and x.start_time <= arrive_time <= x.end_time, lambda x: x.price_per_hour, x.max_stay_hours)
        return price, max_stay_hours