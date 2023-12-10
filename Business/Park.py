from Data.Car import Car
from Data.ParkingTicket import ParkingTicket
from Exception.CarException import CarException
from Utils import FileHelper
class Park:
    def __init__(self, cars: []):
        self.cars = cars
    def park_car(self, car: Car, parking_ticket):
        existed_car = next((c for c in self.cars if c.identity == car.identity), None)
        if existed_car is None:
            self.cars.append(car)
            existed_car = car
        elif existed_car.is_parking():
            raise CarException("Car is already parked.")
        existed_car.parking_tickets.append(parking_ticket)
        FileHelper.write_to_file(self.cars)