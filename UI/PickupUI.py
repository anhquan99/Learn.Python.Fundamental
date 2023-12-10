from UI.BaseUI import BaseUI
from Business.Pickup import Pickup
import Validation.CarValidation as car_validator
import Validation.DateValidation as date_validator

class PickupUI(BaseUI):
    def __init__(self):
        self.__pickup = None
    def input_pickup_info(self):
        global cars
        global price_list
        car_id = self.input_car_id()
        exist_time = self.input_time("Exist time")
        pickup = Pickup(cars, price_list)
        __pickup = pickup
        try:
            temporary_ticket, available_credit = pickup.get_pickup_ticket(car_id, exist_time)
            print("Your information:")
            print(f"Car: {car_id}")
            print(f"Frequent parking number: : {temporary_ticket.fqn}")
            print(f"Discount: : { 'Yes' if temporary_ticket.is_valid_fqn else 'No'}")
            print(f"Arrive time: {temporary_ticket.arrive_time}")
            print(f"Exist time: {temporary_ticket.exist_time}")
            print(f"Available credit: ${available_credit}")
            print("-"*20)
            print(f"Amount: ${temporary_ticket.price}")
            self.check_out()
        except ex:
            print(ex.message)   
    def check_out(self):
        while True:
            try:
                pay_amount = self.input_pay_amount()
                if pay_amount == -1:
                    return
                pickup.checkout(pay_amount)
                print("Thank you for using our service.")
                return
            except ex:
                print(ex.message)
    @car_validator.validate_number
    def input_pay_amount(self):
        while True:
            try:
                fqn = input("You payment amount (input -1 to cancel): ")
                return arrive_time
            except ex:
                print(ex.message)        
        
        