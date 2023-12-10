from Exception import CarException
class History:
    __date_format = "%m-%d-%Y, %H:%M"
    def __init__(self, cars: []):
        self.cars = cars
    def export_history_of_car(self, car_id):
        car = next((c for c in self.cars if c.identity == car_id), None)
        if car is None:
            raise CarException("Car not found.")
        total_payment = 0
        parked_date_str = ""
        for ticket in car.parking_tickets:
            if ticket.exist_time is not None:
                parked_date_str += str(ticket.arrive_time.strftime(self.__date_format)) + " - " + str(ticket.exist_time.strftime(self.__date_format)) + "$%.1f\n" % ticket.price + "\n"
                total_payment += ticket.price
        with open(car_id + ".txt", "w") as f:
            f.write("Total payment: $%.1f\n" % total_payment)
            f.write("Available credit: $%.1f\n" % car.available_credit)
            f.write(parked_date_str)

