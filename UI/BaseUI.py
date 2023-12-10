from Business.Park import Park
import Validation.CarValidation as car_validation
import Validation.DateValidation as date_validator

class BaseUI:
    @car_validation.car_id_validation
    def input_car_id(self):
        print("Please input your car ID")
        while True:
            try:
                car_id = input("Car ID: ")
                return car_id
            except ex:
                print(ex.message)
    @date_validator.validate_date
    def input_time(self, title):
        while True:
            try:
                arrive_time = input(f"{title} (YYYY-MM-DD HH:MM): ")
                return arrive_time
            except ex:
                print(ex.message)