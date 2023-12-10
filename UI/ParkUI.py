from UI.BaseUI import BaseUI
from Business.Park import Park
import Validation.CarValidation as validation

class ParkUI(BaseUI):
    def input_park_info(self):
        global cars
        car_id = self.input_car_id()
        arrive_time, fqn = self.input_parking_ticket()
        park = Park(cars)
        park.park_car(car_id, arrive_time, fqn)

    def input_parking_ticket(self):
        print("Please input your parking ticket")
        arrive_time = self.input_time("Arrive time")
        fqn = self.input_fqn()
        return arrive_time, fqn

    @validation.validate_number
    def input_fqn(self):
        while True:
            try:
                fqn = input("Frequent parking number: ")
                return arrive_time
            except ex:
                print(ex.message)