from Data.Car import Car
from Data.ParkingTicket import ParkingTicket
from Exception import CarException
class Park:
    def __init__(self, cars: []):
        self.cars = cars
    def park_car(self, car: Car, parking_ticket: ParkingTicket):
        existed_car = next((c for c in self.cars if c.identity == car.identity), None)
        if existed_car is None:
            self.cars.append(car)
        elif existed_car.is_parking():
            raise CarException("Car is already parked")
        existed_car.parking_tickets.append(parking_ticket)