import datetime
import numpy as np
from copy import deepcopy
from Data import Car, ParkDay
from Utils import FileHelper
from Exception import CarException, ParkingException

class Pickup:
    def __init__(self, cars: [Car], price_list: (ParkDay)):
        self.__cars = cars
        self.__picking_up_car = None
        self.__picking_up_ticket = None
        self.__exist_time = None
        self.__ticet_price = None
        self.__price_list = price_list

    def get_pickup_ticket(self, car_id, exist_time):
        existed_car = next((c for c in self.__cars if c.identity == car_id), None)
        if existed_car is None:
            raise CarException("Car not found.")
        self.__picking_up_car = existed_car
        current_parking_ticket = existed_car.get_current_parking_ticket()
        if current_parking_ticket is None: 
            raise CarException("Car is not parked.")
        self.__picking_up_ticket = current_parking_ticket
        parked_time = np.float32((exist_time - current_parking_ticket.arrive_time).seconds / 3600)
        if parked_time < 0:
            raise ParkingException.ParkingException("Pick up time can not be before arrive time.")
        self.__exist_time = exist_time
        temporary_ticket = deepcopy(current_parking_ticket)
        temporary_ticket.exist_time = exist_time
        temporary_ticket.price = self.__calculate_price(parked_time)
        self.__ticet_price = temporary_ticket.price
        return temporary_ticket

    def checkout(self, pay_amount):
        balance_credit = self.__picking_up_car.available_credit + pay_amount
        if balance_credit < self.__ticet_price:
            raise ParkingException.ParkingException("Not enough credit.")
        self.__picking_up_ticket.exist_time = self.__exist_time
        self.__picking_up_ticket.price = self.__ticet_price
        self.__picking_up_car.available_credit = balance_credit - self.__ticet_price
        FileHelper.write_to_file(self.__cars)

    def __calculate_price(self, parked_time):
        price_per_hour, max_stay_hours = self.__get_price_on_day()
        if price_per_hour is None:
            raise ParkingException.ParkingException("Some thing wrong with the price list.")

        # get discount
        discount = 0
        if self.__picking_up_ticket.is_valid_fqn:
            if datetime.time(17, 0) < self.__picking_up_ticket.arrive_time.time() < datetime.time(23, 59) or datetime.time(0, 0) < self.__picking_up_ticket.arrive_time.time() < datetime.time(7, 59,):
                discount = 0.5
            else:
                discount = 0.1
        # none is calculated as 1
        if max_stay_hours == 'None':
            return price_per_hour * (1 - discount)

        # calcaulate exceed time
        exceed_time = 0
        if max_stay_hours == "Up to midnight":
            if self.__exist_time.date() != self.__picking_up_ticket.arrive_time.date():
                start_new_date = self.__picking_up_ticket.arrive_time.date()
                start_new_date = start_new_date + timedelta(days=1)
                start_new_date = start_new_date.replace(hour=0, minute=0, second=0, microsecond=0)
                exceed_time = np.float32((self.__picking_up_ticket.exist_time - start_new_date).seconds / 3600)
        elif parked_time > np.intc(max_stay_hours):
            exceed_time = parked_time - np.intc(max_stay_hours)
        return price_per_hour * ((parked_time - exceed_time) + (exceed_time * 2)) * (1 - discount)

    def __get_price_on_day(self):
        day = self.__picking_up_ticket.arrive_time.weekday()
        arrive_time = self.__picking_up_ticket.arrive_time.time()
        x = next((i for i in self.__price_list if i.day_of_week == day), None)
        if x is None or x.park_hours is None:
            raise ParkingException.ParkingException("Some thing wrong with the price list.")        
        rs = tuple(filter(lambda x: x.start_time <= arrive_time <= x.end_time, x.park_hours))
        if len(rs) == 0:
            raise ParkingException.ParkingException("Some thing wrong with the price list.")        
        return np.float32(rs[0].price_per_hour), rs[0].max_stay_hours