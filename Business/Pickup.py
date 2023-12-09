from copy import deepcopy
from Data.Car import Car
from Data.ParkingTicket import ParkingTicket
from Exception import CarException, ParkingException

class Pickup:
    def __init__(self, cars: [], parking_hours: ()):
        self.__cars = cars
        self.__picking_up_car = None
        self.__picking_up_ticket = None
        self.__exist_time = None
    def get_pickup_ticket(self, car_id, exist_time):
        existed_car = next((c for c in self.__cars if c.identity == car_id), None)
        if existed_car is None:
            raise CarException("Car not found")
        self.__picking_up_car = existed_car
        current_parking_ticket = existed_car.get_current_parking_ticket()
        if current_parking_ticket is None: 
            raise CarException("Car is not parked")
        self.__picking_up_ticket = current_parking_ticket
        parked_time = exist_time - current_parking_ticket.arrive_time
        if parked_time < 0:
            raise ParkingException.ParkingException("Pick up time can not be before arrive time")
        self.__exist_time = exist_time
        temporary_ticket = deepcopy(current_parking_ticket)
        temporary_ticket.exist_time = exist_time
        return temporary_ticket